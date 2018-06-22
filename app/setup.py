import os
from setuptools import setup
from setuptools import find_packages
from setuptools.dist import Distribution
import sys

sys.path.append('.')
from python_template.version import VERSION


# to build run: `python setup.py bdist_wheel`


class BinaryDistribution(Distribution):
  def is_pure(self):
    return False


def read_file(*path):
  return open(os.path.join(*path)).read()


def get_requirements(*requirements_path):
  requirements = []
  for requirement in open(os.path.join(*requirements_path)).readlines():
    requirement = requirement.strip()
    requirements.append(requirement)
  return requirements


def main():

  setup_folder = os.path.abspath(os.path.dirname(__file__))
  package = 'python_template'

  os.chdir(setup_folder)

  setup(
    name=package,
    version=VERSION,
    author='rc2',
    author_email='',
    description='python template',
    url='https://github.com/rc2/python-template',
    packages=find_packages(exclude=['test']),
    long_description=read_file(setup_folder, 'README.md'),
    distclass=BinaryDistribution,
    install_requires=get_requirements(setup_folder, 'requirements.txt'),
    entry_points={
      'console_scripts': [
        '{command} = {package}.{file}:{entrypoint}'.format(
          command='app',
          package=package,
          file='app',
          entrypoint='main',
        )
      ]
    }
  )


if __name__ == "__main__":
  main()
