# README

This is an example python template.


## Requirements

- pip
- pipenv

```bash
pip install pipenv --user
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
PYTHONPATH=app python ./app/python_template/cli.py
```

### Add dependencies

Install a package

```bash
pipenv install PACKAGE
```

Install a package used in development only

```bash
pipenv install --dev PACKAGE
```

Update the `requirements.txt` file

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

- **context**: from within a `pipenv` shell

```bash
pip install --user ./app/dist/*
```

#### From git repo sub-folder

```
pip install --user 'git+https://github.com/rc2/python-template.git@develop#wheel=python_template&subdirectory=app'
```

### Use

```bash
python_template help
```

### Uninstall

**container**

```
yes | pip uninstall python_template
```

---
