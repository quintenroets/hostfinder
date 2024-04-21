import hostfinder


def test_find() -> None:
    hostfinder.find_host(timeout=1)


def test_find_multiple() -> None:
    hosts = hostfinder.find_hosts(timeout=1)
    assert isinstance(hosts, list)
