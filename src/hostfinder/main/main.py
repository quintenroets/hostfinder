from ..models import Options
from .hostfinder import HostFinder


def find_hosts(options: Options) -> list[str]:
    hosts = HostFinder(options).find_hosts()
    return list(hosts)


def find_host(options: Options) -> str | None:
    options.show_progress = False
    hosts = HostFinder(options).find_hosts()
    return next(hosts, None)
