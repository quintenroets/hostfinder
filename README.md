# Host finder
[![PyPI version](https://badge.fury.io/py/hostfinder.svg)](https://badge.fury.io/py/hostfinder)
![PyPI downloads](https://img.shields.io/pypi/dm/hostfinder)
![Python version](https://img.shields.io/badge/python-3.10+-brightgreen)
![Operating system](https://img.shields.io/badge/os-linux%20%7c%20macOS%20%7c%20windows-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

Find hosts listening on specified port in local network

## Usage
1) Command line

    ```shell
    hostfinder --port 8080
    ```

2) Python module

    ```python
    import hostfinder
    from hostfinder import Options

    options = Options(port=8080)

    # first host listening on a port
    host = hostfinder.find_host(options)

    # all hosts listening on a port
    hosts = hostfinder.find_hosts(options)
    ```

## Installation
```shell
pip install hostfinder
```
