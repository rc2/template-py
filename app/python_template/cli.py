#!python
"""
python_template

usage:
  python_template debug
  python_template echo <text>
  python_template hello
  python_template help

"""
from docopt import docopt
import sys
import os

from python_template.version import VERSION


def main():
  args = docopt(__doc__, version=VERSION)
  if args['debug']:
    print(args)
    return
  if args['echo']:
    print(args['<text>'])
    return
  if args['hello']:
    print("hello")
    return
  if args['help']:
    print(__doc__)
    return
  print(__doc__)


if __name__ == "__main__":
  main()
