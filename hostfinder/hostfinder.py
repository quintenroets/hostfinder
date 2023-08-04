import concurrent.futures
import ipaddress
import socket
from dataclasses import dataclass

import psutil


@dataclass
class HostFinder:
    port: int = 22
    loopback_name: str = "lo"
    timeout: int = 10

    def __post_init__(self):
        socket.setdefaulttimeout(self.timeout)

    def generate_hosts(self):
        possible_hosts = self.local_subnet_addresses()
        possible_hosts = list(possible_hosts)
        num_possible_hosts = len(possible_hosts)
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=num_possible_hosts)
        with executor:
            results = executor.map(self.is_listening, possible_hosts)
            for result in results:
                if result is not None:
                    yield result

    def local_subnets(self):
        local_interfaces = psutil.net_if_addrs()
        for interface_name, subnets in local_interfaces.items():
            if interface_name != self.loopback_name:
                yield from subnets

    def local_subnet_addresses(self):
        for subnet in self.local_subnets():
            if subnet.family == socket.AF_INET:
                network_string = f"{subnet.address}/{subnet.netmask}"
                network = ipaddress.IPv4Network(network_string, strict=False)
                for address in network.hosts():
                    yield str(address)

    def is_listening(self, address: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            connection_result = sock.connect_ex((address, self.port))
        result = address if connection_result == 0 else None
        return result
