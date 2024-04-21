import hostfinder
from hostfinder import Options


def test_find_host() -> None:
    options = Options(timeout=1)
    host = hostfinder.find_host(options)
    assert host is None or isinstance(host, str)


def test_find_hosts() -> None:
    options = Options(timeout=1)
    hosts = hostfinder.find_hosts(options)
    assert isinstance(hosts, list)
