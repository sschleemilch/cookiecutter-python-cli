import logging

import rich_click as click
from rich.logging import RichHandler
from rich.traceback import install

from . import __version__


FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", 
    format=FORMAT, 
    datefmt="[%X]", 
    handlers=[RichHandler(rich_tracebacks=True)]
)

log = logging.getLogger("{{cookiecutter.package_name}}")

def set_log_level(verbose: int) -> None:
    if verbose > 2:
        log.setLevel("DEBUG")
        install(show_locals=True)
    elif verbose > 1:
        log.setLevel("INFO")
    elif verbose > 0:
        log.setLevel("WARNING")
    else:
        log.setLevel("ERROR")

@click.command()
@click.option("-v", "--verbose", count=True, help="Verbositiy level, can be given up to 3 times (-vvv)")
@click.version_option(__version__)
def main(
    verbose: int):

    set_log_level(verbose)

    log.info("Running {{cookiecutter.package_name}}")
    log.debug("Debugging infos")

if __name__ == "__main__":
    main()
