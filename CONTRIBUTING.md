# Contributing to img360-transformer

Thank you for considering contributing to this project!

## For Everyone

- **Code Formatting:**
  - Use [Black](https://black.readthedocs.io/en/stable/) for code formatting and [isort](https://pycqa.github.io/isort/) for import sorting.
  - Install both tools with Poetry (dev group):
    ```bash
    poetry install --with dev
    ```
  - Run both tools before submitting a pull request:
    ```bash
    black .
    isort .
    ```

## For Me

- **Version Bumping:**
  - Update the version in `pyproject.toml` as needed.
- **Publishing:**
  - Use Poetry to build and publish:
    ```bash
    poetry build
    poetry publish
    ```
