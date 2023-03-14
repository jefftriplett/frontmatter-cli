@_default:
    just --list

@fmt:
    just --fmt --unstable

@bootstrap:
    pip install --upgrade pip pip-tools
    pip install --requirement=requirements.in --upgrade
    pre-commit autoupdate

@build:
    python -m build

@bump *ARGS="--dry":
    bumpver update {{ ARGS }}

@check:
    twine check dist/*

@lint *ARGS="--all-files":
    pre-commit run {{ ARGS }}

@nox:
    nox

@pip-compile:
    pip-compile

@push:
    git push origin --all

@test:
    pytest

@update:
    pip install -U pip pip-tools

@upload:
    twine upload dist/*
