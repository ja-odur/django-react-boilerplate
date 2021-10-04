from invoke import Collection
from .testing import lint_js
from .dev import (
    prettier_js,
    build_prod,
    webpack_dev_server,
    python_server
)

task_col = Collection()

task_col.add_task(lint_js)
task_col.add_task(prettier_js)
task_col.add_task(build_prod)
task_col.add_task(webpack_dev_server)
task_col.add_task(python_server)
