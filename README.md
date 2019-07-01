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

## How to

### Setup

#### Install `pipenv`

```bash
pip3 install pipenv --user
```

#### Get this template repository

```bash
curl -s -L https://github.com/rc2/template-py/archive/master.zip -o template-py.zip \
  && unzip -qq template-py.zip \
  && mv template-py-master PROJECT_NAME \
  && rm template-py.zip
```

#### Install dependencies and setup virtual environment

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
```

### Development

#### Start the development shell

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv shell
```

#### Interactive development

*Running the applications command line tool (during development mode)*

- Sets `PYTHONPATH` to the `./app` folder and run the command line interface
- Runs the command line interface (`cli.py`)

```bash
PYTHONPATH=app python3 ./app/template_py/cli.py
```

### Dependency Management

#### Install a dependency

```bash
pipenv install PACKAGE_NAME \
  && pipenv lock -r > ./app/requirements.txt
```

#### Install a development dependency

```bash
pipenv install --dev PACKAGE_NAME
```

#### Update the `requirements.txt` file

```bash
pipenv lock -r > ./app/requirements.txt
```

### Testing

#### Defining a *Feature*

- Using gherkin syntax (given/when/then)
- See https://pypi.org/project/pytest-bdd/

#### Convert features into test files

```bash
pytest-bdd generate ./app/test/features/FEATURE.feature > ./app/test/test_FEATURE.feature
```

#### Run all tests

- **context**: from within a `pipenv` shell

```bash
pytest
```

### Packaging

#### Build

- **context**: from within a `pipenv` shell

```bash
python app/setup.py bdist_wheel
```

#### Install

##### From build directory

```bash
pip3 install --user ./app/dist/template_py-$(cat ./app/template_py/VERSION)-py3-none-any.whl
```

##### From git repo sub-folder

*Example*

###### Install directly from the `master` branch of this repository

```
pip3 install --user 'git+https://github.com/rc2/template-py.git@master#wheel=template_py&subdirectory=app'
```

###### Install directly from the `develop` branch of this repository

```
pip3 install --user 'git+https://github.com/rc2/template-py.git@develop#wheel=template_py&subdirectory=app'
```

### Usage

```bash
template_py help
```

### Uninstall

```
pip3 uninstall -y template_py
```

---
