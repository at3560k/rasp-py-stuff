"""Console script for wpower."""

import sys

import typer

from wpower.remote import Outlet

app = typer.Typer()


@app.command()
def power_on():
    """ On """
    outlet = Outlet()
    outlet.power_on()
    typer.echo("On")


@app.command()
def power_off():
    """ off """
    outlet = Outlet()
    outlet.power_off()
    typer.echo("Off")


@app.command()
def msg():
    """
    pass basic test
    """
    typer.echo("Replace this message by putting your code into " "wpower.cli.main")
    typer.echo("See click documentation at https://click.palletsprojects.com/")


def main(args=None):
    """Console script for wpower."""
    app()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
