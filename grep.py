import argparse
import sys


def output(line):
    print(line)


def grep(lines, params):
    for line in lines:
        line = line.rstrip()
        if params.pattern in line:
            output(line)


def parse_args(args):


def main():
    params = parse_args(sys.argv[1:])
    grep(sys.stdin.readlines(), params)


if __name__ == '__main__':
    main()
