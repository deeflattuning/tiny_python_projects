#!/usr/bin/env python3
"""
Author: Sandy Rodriguez <sandy.d.rodriguez@outlook.com>
Purpose: To give a friendly greeting
"""

import argparse


def get_args():
    """Get command line arguments"""


    parser = argparse.ArgumentParser(description="A friendly program that says hello!")
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help="Name to greet")
    return parser.parse_args()


def main():
    """This is the main function"""


    args = get_args()
    print ("Hello, " + args.name + "!")


if __name__ == '__main__':
    main()
