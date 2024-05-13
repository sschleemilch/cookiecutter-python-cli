import logging

import rich_click as click
from rich.logging import RichHandler
from rich.traceback import install
from pathlib import Path

from . import __version__

logging.basicConfig(level="INFO", format="%(message)s",
                    datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True)])

log = logging.getLogger("{{cookiecutter.package_name}}")


@click.command()
@click.option("-l", "--log-level", type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False), default="INFO", help="Log level", show_default=True)
@click.option("--log-file", type=click.Path(dir_okay=False, writable=True, path_type=Path), help="Log file")
@click.version_option(__version__)
def cli(log_level: str, log_file: Path | None) -> None:
    if log_file:
        file_handler = logging.FileHandler(log_file, mode="w")
        file_handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(message)s"))
        log.addHandler(file_handler)

    log.setLevel(log_level)
    if log_level == "DEBUG":
        install(show_locals=True)

    log.info("Running {{cookiecutter.package_name}}")
    log.debug("Debugging infos")


def main() -> None:
    cli(auto_envvar_prefix="{{cookiecutter.package_name}}")
