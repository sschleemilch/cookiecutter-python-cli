#!/usr/bin/env python
import subprocess
from pathlib import Path

if __name__ == "__main__":
    if "{{ cookiecutter.git }}" == "y":
        _ = subprocess.check_call(["git", "init", "-b", "main"])
    else:
        Path(".gitignore").unlink()
        Path(".pre-commit-config.yaml").unlink()

    _ = subprocess.check_call(["uv", "sync", "-U"])

    if "{{ cookiecutter.nox }}" != "y":
        Path("noxfile.py").unlink()

    if "{{ cookiecutter.dockerfile }}" != "y":
        Path("Dockerfile").unlink()
        Path(".dockerignore").unlink()
