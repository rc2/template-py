# README

## clean

```
find . -type d -iname "__pycache__" -exec rm -r {} \;
```

## install dependencies

```
pip install -r requirements.txt
```

## run tests

```
pytest
```

## build

```
python setup.py bdist_wheel
```

## install app

```
pip install dist/*
```

## uninstall app

```
yes | pip uninstall package
```

---

## examples

### pip install package from repo

```
pip install git+https://github.com/rc2/python-template.git@BRANCH#wheel=PACKAGE_NAME
```

### pip install package from repo subfolder

```
pip install git+https://github.com/rc2/python-template.git@BRANCH#wheel=PACKAGE_NAME&subdirectory=SUBFOLDER
```
