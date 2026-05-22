from typing import Optional

import typer

app = typer.Typer(
    help="QR code generator from the terminal using a URL",
    epilog="¡Thanks for using juadaqr! ",
)


def version_callback(value: bool):
    if value:
        typer.echo("juadaqr v0.1.0")
        raise typer.Exit()


@app.callback()
def main(
    _version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=version_callback,
        is_eager=True,
    ),
):
    pass
