import logging

import rich_click as click
from rich.logging import RichHandler
from rich.traceback import install

from {{cookiecutter.package_name}} import __version__


FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", 
    format=FORMAT, 
    datefmt="[%X]", 
    handlers=[RichHandler(rich_tracebacks=True)]
)

logger = logging.getLogger("{{cookiecutter.package_name}}")

def configure_run_mode(verbose: int) -> None:
    if verbose > 2:
        logger.setLevel("DEBUG")
        install(show_locals=True)
    elif verbose > 1:
        logger.setLevel("WARNING")
    elif verbose > 0:
        logger.setLevel("INFO")
    else:
        logger.setLevel("ERROR")

@click.command()
@click.option("-v", "--verbose", count=True, help="Verbositiy level, can be given up to 3 times (-vvv)")
@click.version_option(__version__)
def main(
    verbose: int):

    configure_run_mode(verbose)

    logger.info("Running {{cookiecutter.package_name}}")
    logger.debug("Debugging infos")

if __name__ == "__main__":
    main()
