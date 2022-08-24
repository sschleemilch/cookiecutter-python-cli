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

def configure_run_mode(debug: bool):
    if debug:
        logger.setLevel("DEBUG")
    install(show_locals=debug)

@click.command()
@click.option("--debug", is_flag=True, help="Enables debug outputs.")
@click.option("--version", "-V", is_flag=True, help="Print version and exit.")
def main(
    version: bool = False, 
    debug: bool = False):
    """ main cli entry point """

    configure_run_mode(debug)

    if version:
        print(__version__)
        return

    logger.info("Running {{cookiecutter.package_name}}")
    logger.debug("Debugging infos")

if __name__ == "__main__":
    main()
