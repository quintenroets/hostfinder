import ipaddress
import socket
from collections.abc import Callable, Iterator
from dataclasses import dataclass, field
from typing import cast

import cli
import psutil
from package_utils.jobs import run_jobs

from hostfinder.models import Address, Options


@dataclass
class HostFinder:
    options: Options = field(default_factory=Options)
    loopback_name: str = "lo"

    def __post_init__(self) -> None:
        socket.setdefaulttimeout(self.options.timeout)

    def find_hosts(self) -> Iterator[str]:
        def create_job(host: str) -> Callable[[], str | None]:
            return lambda: self.extract_listening_address(host)

        jobs = [create_job(host) for host in self.generate_host_addresses()]
        results = run_jobs(jobs, number_of_workers=self.options.max_workers)
        if self.options.show_progress:
            results = cli.track_progress(
                results,
                total=len(jobs),
                description="Checking",
                unit="addresses",
            )
        return (result for result in results if result is not None)

    def generate_subnets(self) -> Iterator[Address]:
        interfaces = psutil.net_if_addrs()
        for name, subnets in interfaces.items():
            if name != self.loopback_name:
                yield from cast(Iterator[Address], subnets)

    def generate_host_addresses(self) -> Iterator[str]:
        for subnet in self.generate_subnets():
            if subnet.family == socket.AF_INET and subnet.netmask.count("0") == 1:
                subnet_string = f"{subnet.address}/{subnet.netmask}"
                network = ipaddress.IPv4Network(subnet_string, strict=False)
                for address in network.hosts():
                    yield str(address)

    def extract_listening_address(self, host: str) -> str | None:
        address = host, self.options.port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_:
            connection_result = socket_.connect_ex(address)
        return host if connection_result == 0 else None
