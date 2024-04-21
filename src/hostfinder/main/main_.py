from .hostfinder import HostFinder


def find_hosts(**kwargs):
    hosts = generate_hosts(**kwargs)
    return list(hosts)


def find_host(**kwargs):
    hosts = generate_hosts(**kwargs)
    try:
        host = next(hosts)
    except StopIteration:
        host = None
    return host


def generate_hosts(**kwargs):
    return HostFinder(**kwargs).generate_hosts()
