from dataclasses import dataclass


@dataclass
class Address:
    family: int
    address: str
    netmask: str
    broadcast: str
    ptp: bool
