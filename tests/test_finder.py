import hostfinder


def test_find():
    hostfinder.find_host(timeout=1)


def test_find_multiple():
    hosts = hostfinder.find_hosts(timeout=1)
    assert isinstance(hosts, list)
