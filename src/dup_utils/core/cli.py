from __future__ import annotations

import sys
from pathlib import Path

import click

from .scripts.git import cli_git


@click.group()
def cli():
    """A simple command line tool."""
    pass  # pragma: no cover.


@cli.command()
@click.argument("path", type=click.Path(exists=True, resolve_path=True))
def ls(path: str):
    for file in Path(path).glob("*"):
        print(f"> {file.resolve()}")
    sys.exit("Hello World")


@cli.command()
def say():
    sys.exit("Hello World")


def main() -> None:
    cli.add_command(cli_git)
    cli.main()


if __name__ == "__main__":
    main()
