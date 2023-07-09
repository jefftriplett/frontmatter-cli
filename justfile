@_default:
    just --list

@fmt:
    just --fmt --unstable

@bootstrap:
    pip install --upgrade pip pip-tools
    pip install .
    pip install .[build]
    pre-commit autoupdate

@build:
    python -m build

@bump *ARGS:
    bumpver update {{ ARGS }}

@bump-dry *ARGS:
    just bump --dry {{ ARGS }}

@check:
    twine check dist/*

@lint *ARGS="--all-files":
    pre-commit run {{ ARGS }}

@nox:
    nox

@pip-compile:
    pip-compile --resolver=backtracking pyproject.toml
    # pip-compile --extra=dev --resolver=backtracking pyproject.toml

@push:
    git push origin --all

@test:
    pytest

@update:
    pip install -U pip pip-tools

@upload:
    twine upload dist/*
