#! /usr/bin/env python3
# Purpose: Say Hello

import argparse

def get_args() -> str:
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n','--name', metavar='name',
                        default='World',
                        help='Name to greet')
    return parser.parse_args()

def main() -> None:
    args = get_args()
    print(f'Hello {args.name}!')



if __name__ == '__main__':
    main()
