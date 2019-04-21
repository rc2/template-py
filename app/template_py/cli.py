#!python
"""
template_py

usage:
  template_py debug
  template_py echo <text>
  template_py hello
  template_py help

"""
from docopt import docopt
import sys
import os

from template_py.version import VERSION


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
