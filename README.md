# README

## Purpose

This is an example template meant for development of python packages. It is meant to be simple to adapt and get a new python project up and running.

## Notes

- Uses `pipenv` for easy setup
- The sub-folder `app/` contains the project source
- Tests are run using `pytest`
  - Gherkin "features" are supported with [`pytest-bdd`](https://pypi.org/project/pytest-bdd/)


## Requirements

- python3
- pip3
- pipenv

```bash
pip3 install pipenv --user
```

## How to

### Install dependencies and setup virtual environment

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
```

### Start the development shell

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv shell
```

### Run the app's command line tool (during development mode)

- Set `PYTHONPATH` to the `./app` folder and run the command line interface

```bash
PYTHONPATH=app python ./app/template_py/cli.py
```

### Add dependencies

#### Install a package

```bash
pipenv install PACKAGE
```

#### Install a package used in development only

```bash
pipenv install --dev PACKAGE
```

#### Update the `requirements.txt` file

```bash
pipenv lock -r > ./app/requirements.txt
```

### Convert features into test files

```bash
pytest-bdd generate ./app/test/features/FEATURE.feature > ./app/test/test_FEATURE.feature
```


### Run tests

- **context**: from within a `pipenv` shell

```bash
pytest
```

### Build

- **context**: from within a `pipenv` shell

```bash
python app/setup.py bdist_wheel
```

### Install

#### From build directory

```bash
pip3 install --user ./app/dist/template_py-$(cat ./app/template_py/VERSION)-py3-none-any.whl
```

#### From git repo sub-folder

```
pip3 install --user 'git+https://github.com/rc2/template-py.git@develop#wheel=template_py&subdirectory=app'
```

### Use

```bash
template_py help
```

### Uninstall

```
pip3 uninstall -y template_py
```

---
