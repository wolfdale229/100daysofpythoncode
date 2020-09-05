#! /usr/bin/env python3
"""
Author : Omefe Chika
Purpose :Say hello
"""

import argparse


def get_args():
    """ Get a person's first name and second name and prints
    a customized greeting for the peson. If either names are
    not given it uses the default value.
    parameters:
        firstname : person first name
        secondname : person's second name
        default : default value to print (World)
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-fn',
                        '--firstname',
                        metavar='first name',
                        default='World!',
                        help='Add first name')
    parser.add_argument('-sn',
                        '--secondname',
                        metavar='second name',
                        default='',
                        help='Add second name')
    return parser.parse_args()


def main():
    """Main Program"""
    args = get_args()
    print(f'Hello! {args.firstname} {args.secondname} !')  # greet the person


if __name__ == '__main__':
    main()
