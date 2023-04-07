import logging

import rich_click as click
from rich.logging import RichHandler
from rich.traceback import install

from . import __version__

logging.basicConfig(level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True)])

log = logging.getLogger("{{cookiecutter.package_name}}")

@click.command()
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose output.")
@click.version_option(__version__)
def main(verbose: bool):

    if verbose:
        log.setLevel(logging.DEBUG)
        install(show_locals=True)

    log.info("Running {{cookiecutter.package_name}}")
    log.debug("Debugging infos")


if __name__ == "__main__":
    main()
