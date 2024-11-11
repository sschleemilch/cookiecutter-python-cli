import nox

PYTHON_VERSIONS = ["3.11", "3.12", "3.13"]

nox.options.default_venv_backend = "uv"


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    session.run_install(
        "uv",
        "sync",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run(
        "pytest",
        "--cov={{cookiecutter.package_name}}",
        "--cov-report=term-missing",
        "--cov-fail-under=0",
        *session.posargs,
    )
