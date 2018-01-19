#!python
"""
app

usage:
  app -e ECHO [ -h -d ]

arguments:
  -e,--echo=ECHO            echo text back to screen

options:
  -h,--help                 get help
  -d,--debug                print debug info
"""
from docopt import docopt


def main():
  args = docopt(__doc__)
  if args['-d']:
    print(args)
  print(args['ECHO'])


if __name__ == "__main__":
  main()
