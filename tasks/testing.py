from invoke import run, task


@task(name='lint-js')
def lint_js(context):
    """lint the javascript files"""
    run('bin/tests/check_prettier_errors.sh --all', echo=True)
