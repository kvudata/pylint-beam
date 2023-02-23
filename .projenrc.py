from projen import ProjectType, TaskStep
from projen.python import PythonProject

project = PythonProject(
    author_email="kvudata@gmail.com",
    author_name="Krishna Vudata",
    module_name="pylint_beam",
    name="pylint-beam",
    homepage="https://github.com/kvudata/pylint-beam",
    description="Pylint plugin for Apache Beam",
    version="0.1.1",
    project_type=ProjectType.LIB,
    deps=[
        "pylint@2.*",
        "astroid",
        # ^ is explicitly stating the requirement since we import it, but not pinning since we expect this dep to come
        # through pylint
    ],
    dev_deps=[
        "pytest",
    ],
)

# add a task to be able to start a repl or run tests with --pdb
project.add_task("python", exec="python", receive_args=True)
project.add_task("run-plugin", steps=[
    TaskStep(exec="pip install -e ."),  # install the package itself in editable/development mode
    # ref: https://setuptools.pypa.io/en/latest/userguide/development_mode.html
    TaskStep(
        exec="pylint --load-plugins pylint_beam.checkers --disable all --enable write-to-bq",
        receive_args=True,
    ),
])

project.synth()
