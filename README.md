# README

This is an example python template.


## Requirements

- make
- docker
- docker-compose

## How to


### Use developer container

**host**

```bash
make console
```

### Building developer container (without launching)

**host**

```bash
make env-build
```

**host**

Force rebuild

```bash
make env-rebuild
```

### Run tests

**host**

```bash
make test
```

**container**

```bash
pytest
```

### Build

**container**

```bash
python setup.py bdist_wheel
```

### Install

#### From build directory

**container**

```bash
pip install --user dist/*
```

### From git repo sub-folder

```
pip install --user 'git+https://github.com/rc2/python-template.git@develop#wheel=python_template&subdirectory=app'
```

### Uninstall

**container**

```
yes | pip uninstall python-template
```

---
