from nox_poetry import session

PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11"]


@session(python=PYTHON_VERSIONS)
def tests(session):
    session.install("pytest", ".")
    session.run("pytest")


@session(python=PYTHON_VERSIONS)
def typing(session):
    session.install("mypy", ".")
    session.run("mypy")
