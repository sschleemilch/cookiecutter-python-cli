from nox_poetry import session

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12"]


@session(python=PYTHON_VERSIONS)
def tests(session):
    session.install("pytest", "pytest-cov", ".")
    session.run("pytest", "--cov={{cookiecutter.package_name}}",
                "--cov-report=term-missing", "--cov-fail-under=0", *session.posargs)


@session(python=PYTHON_VERSIONS)
def typing(session):
    session.install("mypy", ".")
    session.run("mypy", "--install-types",
                "--non-interactive", *session.posargs)
