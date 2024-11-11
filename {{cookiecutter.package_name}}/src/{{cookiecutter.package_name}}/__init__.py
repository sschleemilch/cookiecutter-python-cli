import logging
from rich.logging import RichHandler

__author__ = """{{cookiecutter.author_name}}"""
__email__ = "{{cookiecutter.author_email}}"
__version__ = "{{cookiecutter.version }}"

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

log = logging.getLogger("{{cookiecutter.package_name}}")
