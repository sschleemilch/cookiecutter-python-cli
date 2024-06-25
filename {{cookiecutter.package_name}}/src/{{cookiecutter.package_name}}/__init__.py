from importlib import metadata
import logging
from rich.logging import RichHandler

__author__ = """{{cookiecutter.author_name}}"""
__email__ = "{{cookiecutter.author_email}}"
__version__ = metadata.version("{{cookiecutter.package_name }}")

logging.basicConfig(level="INFO", format="%(message)s",
                    datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True)])

log = logging.getLogger("{{cookiecutter.package_name}}")
