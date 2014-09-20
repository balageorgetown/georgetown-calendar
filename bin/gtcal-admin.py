__author__ = 'bvenkatesan'

import os
import sys

import argparse
sys.path.append("/Users/bvenkatesan/Documents/workspace/PyCharmProjects/georgetown-calendar")
import gtcal

DESCRIPTION = "A simple calendar app on the command line"
VERSION = "1.0.0"
EPILOG  = "NO BUGS PLEASE"

def main(*argv):
    parser = argparse.ArgumentParser(description=DESCRIPTION,version=VERSION,epilog=EPILOG)


if __name__ == "__main__":
    main(sys.argv[1:])