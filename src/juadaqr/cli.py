from importlib.metadata import PackageNotFoundError, version
from typing import Optional

import typer

from .core import generate_qr_terminal

try:
    __version__ = version("juadaqr")
except PackageNotFoundError:
    __version__ = "0.1.0-dev"

app = typer.Typer(
    help="QR code generator from the terminal using a URL",
    epilog="¡Thanks for using juadaqr! ",
)


def version_callback(value: bool):
    if value:
        typer.echo(f"juadaqr v{__version__}")
        raise typer.Exit()


@app.command()
def main(
    url: str = typer.Argument(..., help="URL to generate QR code"),
    _version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=version_callback,
        is_eager=True,
    ),
):
    typer.secho(f"Generating QR for {url}", fg=typer.colors.BLUE)

    try:
        qr_ascii = generate_qr_terminal(url)
        typer.echo("\n" + qr_ascii)
        typer.secho(f"\nQR generated for {url}", fg=typer.colors.GREEN)

    except ValueError as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.secho(f"Unexpected error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    typer.secho("Done!", fg=typer.colors.GREEN)
