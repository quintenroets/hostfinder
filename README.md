[![PyPI version](https://badge.fury.io/py/hostfinder.svg)](https://badge.fury.io/py/hostfinder)
# Host finder

Find host in local subnet listening on specified port

## Installation

Make sure you are using python3.10+

 ```shell
 pip install hostfinder
 ```
    
## Usage
1) Command line

```shell
hostfinder --port 8080
```

2) In Python module

```python
import hostfinder

# find first host listening to a port
host = hostfinder.find_host(port=8080)

# find all hosts listening to a port
hosts = hostfinder.find_hosts(port=8080)
```
