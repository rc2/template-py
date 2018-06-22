#!python
"""
app

usage:
  app -e ECHO [ -h -d ]
  app [ -h -v ]

arguments:
  -e,--echo=ECHO            echo text back to screen

options:
  -h,--help                 print help and exit
  -v, --version             print version and exit
  -d,--debug                print debug info
"""
from docopt import docopt
import sys

sys.path.append('.')
from version import VERSION


def main():
  args = docopt(__doc__, version=VERSION)
  if args['--debug']:
    print(args)
  if args['--echo'] and len(args['--echo']) > 0:
    print(args['--echo'])


if __name__ == "__main__":
  main()
