import logging
import rich_click as click
from rich.logging import RichHandler
from rich.traceback import install

from {{cookiecutter.package_name}} import __version__

install(show_locals=True)

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", 
    format=FORMAT, 
    datefmt="[%X]", 
    handlers=[RichHandler(rich_tracebacks=True)]
)

log = logging.getLogger("{{cookiecutter.package_name}}")

@click.command()
@click.option("--debug", is_flag=True, help="Enables debug outputs.")
@click.option("--version", "-V", is_flag=True, help="Print version and exit.")
def main(
    version: bool = False, 
    debug: bool = False):
    """Console script for {{cookiecutter.package_name}}"""
    if version:
        print(__version__)
        return
    if debug:
        log.setLevel("DEBUG")

    log.info(f"Running {{cookiecutter.package_name}}")
    log.debug(f"Debugging infos")

if __name__ == "__main__":
    main()
