# Host finder
[![PyPI version](https://badge.fury.io/py/hostfinder.svg)](https://badge.fury.io/py/hostfinder)
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

    # first host listening on a port
    host = hostfinder.find_host(port=8080)

    # all hosts listening on a port
    hosts = hostfinder.find_hosts(port=8080)
    ```

## Installation
```shell
pip install hostfinder
```
