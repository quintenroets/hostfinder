from package_utils.cli import create_entry_point

from hostfinder import Options
from hostfinder.main.hostfinder import HostFinder


def find_hosts(options: Options) -> None:
    hosts = HostFinder(options).find_hosts()
    output = "\n".join(hosts)
    print(output)  # noqa: T201


entry_point = create_entry_point(find_hosts)
