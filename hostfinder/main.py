import argparse

from . import hostfinder


def main():
    description = "Find host in local subnet listening to specified port"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--port",
        type=int,
        default=22,
        help="Port that host should be listening on",
    )
    args = parser.parse_args()
    kwargs = vars(args)
    hosts = hostfinder.HostFinder(**kwargs).generate_hosts()
    output = "\n".join(hosts)
    print(output)


if __name__ == "__main__":
    main()
