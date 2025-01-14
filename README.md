# Guidelines

## Each repository uses pre-commit checks

* pre-commit >= 4.0.1 installed
* one file ".pre-commit-config.yaml" created
* installed via > pre-commit install


## Development

* poetry is mandatory
    * Each repository contianing python code configures via pyproject.toml
* pipx is recommendet
* ruff configured as linter and formatter (cna be configured in pyproject.toml)

# Style Guidelines

* line length 120
* folder structure like this project:
    * pyproject.toml
    * .pre-commit-config.yaml
    * README.md
    * (project-name)
        * __init__.py
    * tests
        * __init__.py
