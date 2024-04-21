from dataclasses import dataclass
from typing import Annotated

import typer

port_help = "Port that the host should be listening on"


@dataclass
class Options:
    port: Annotated[int, typer.Option(help=port_help)] = 22
    loopback_name: str = "lo"
    timeout: int = 10
    max_workers: int = 100
    show_progress: bool = True
