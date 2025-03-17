import collections

from hostfinder.models import Options

from .hostfinder import HostFinder


def find_hosts(options: Options | None = None) -> list[str]:
    host_finder = HostFinder() if options is None else HostFinder(options)
    return list(host_finder.find_hosts())


def find_host(options: Options | None = None) -> str | None:
    host_finder = HostFinder() if options is None else HostFinder(options)
    host_finder.options.show_progress = False
    hosts = host_finder.find_hosts()
    host = next(hosts, None)
    collections.deque(hosts, maxlen=0)
    return host
