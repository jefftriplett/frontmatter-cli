from invoke import run, task


@task
def git_push(context):
    run("git push origin --all")


@task
def pypi(context):
    run("python setup.py sdist")
    run("python setup.py bdist_wheel")


@task
def pypi_upload(context):
    run("python setup.py sdist upload")
    run("python setup.py bdist_wheel upload")
