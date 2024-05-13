# Contributing to {{cookiecutter.package_name_long}}

## Development Environment

{{cookiecutter.package_name_long}} uses [poetry](https://python-poetry.org/docs/) for packaging and
dependency management. To start developing with {{cookiecutter.package_name_long}}, install Poetry
using the [recommended method](https://python-poetry.org/docs/#installation) or run:

```
pip install poetry
```

{%- if cookiecutter.nix == "y" %}
Alternatively, since there exists a [shell.nix](./shell.nix) you can use `nix-shell` of the [nixos](https://nixos.org/) project to setup a suitable devenv.
{%- endif %}

Once Poetry is installed, install the dependencies with the following command:

```
poetry install
```

Poetry uses virtual environments and handles those for you efficiently.

If you want to have a shell in the virtual environment you can activate it with (for Linux/MacOS):

```
. $(poetry env info --path)/bin/activate
```

The package is linked in editable mode so you will not need to reinstall the package when changing something.

Alternatively you can run things in the virtual environment by using a `poetry run` prefix for commands, e.g.:

```
poetry run pytest
```

**The following section commands assume you are in the poetry installed environment by either activating or prefixing commands with `poetry run`!**

{%- if cookiecutter.git == "y" %}

### Pre-Commit-Hooks

Pre commit hooks can be setup with:

```
pre-commit install
```
{%- endif %}

### Tests

Run tests with the following command:

```
pytest --cov-report term-missing --cov={{cookiecutter.package_name}} -vv
```

New code should ideally have tests and not break existing tests.

### Type Checking

{{cookiecutter.package_name_long}} uses type annotations throughout, and `mypy` to do the checking. Run the following to type check {{cookiecutter.package_name_long}}:

```
mypy --ignore-missing-imports --no-implicit-optional --warn-unreachable
```

### Code Formatting

{{cookiecutter.package_name_long}} uses [`ruff`](https://docs.astral.sh/ruff/) for code formatting.
Since it is very fast it makes sense to setup your editor to format on save.

Use `ruff format` to format all files in the currenct directory

## Optional

If you want to test versus more than one Python version there is a [noxfile.py](noxfile.py) that will run tests and typing checks on all supported Python versions.
You will need to have [nox](https://nox.thea.codes/en/stable/) as well as [nox-poetry](https://github.com/cjolowicz/nox-poetry) installed on your system.
You can then run `nox`. Make sure you are **not** in the virtual environment of the tool when doing so.
