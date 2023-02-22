from projen import ProjectType
from projen.python import PythonProject

project = PythonProject(
    author_email="kvudata@gmail.com",
    author_name="Krishna Vudata",
    module_name="pylint_beam",
    name="pylint-beam",
    version="0.1.0",
    project_type=ProjectType.LIB,
    deps=[
        "pylint@2.*",
    ],
    dev_deps=[
        "pytest",
    ],
)

# add a task to be able to start a repl or run tests with --pdb
project.add_task("python", exec="python", receive_args=True)

project.synth()
