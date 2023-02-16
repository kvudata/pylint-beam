from projen.python import PythonProject

project = PythonProject(
    author_email="kvudata@gmail.com",
    author_name="Krishna Vudata",
    module_name="pylint_beam",
    name="pylint-beam",
    version="0.1.0",
)

project.synth()