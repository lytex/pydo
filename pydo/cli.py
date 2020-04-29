"""
Module to store the command line and logger functions.

Functions:
    load_logger: Function to define the program logging object.
    load_parser: Function to define the command line arguments.
"""

import logging
import argparse
import argcomplete


def load_parser():
    '''
    Function to define the command line arguments.
    '''

    # Argparse
    parser = argparse.ArgumentParser(
        description='CLI task manager built with Python and SQLite.',
    )

    subparser = parser.add_subparsers(dest='subcommand', help='subcommands')
    subparser.add_parser('install')

    add_parser = subparser.add_parser('add')
    add_parser.add_argument(
        "add_argument",
        type=str,
        help='Task add arguments',
        default=None,
        nargs=argparse.REMAINDER,
    )

    modify_parser = subparser.add_parser('mod')
    modify_parser.add_argument(
        "ulid",
        type=str,
        help='Task ulid',
    )
    modify_parser.add_argument(
        "modify_argument",
        type=str,
        help='Task modify arguments',
        default=None,
        nargs=argparse.REMAINDER,
    )

    delete_parser = subparser.add_parser('del')
    delete_parser.add_argument(
        "ulid",
        type=str,
        help='Task ulid',
    )

    complete_parser = subparser.add_parser('done')
    complete_parser.add_argument(
        "ulid",
        type=str,
        help='Task ulid',
    )

    subparser.add_parser('list')
    subparser.add_parser('projects')
    subparser.add_parser('tags')
    subparser.add_parser('export')

    argcomplete.autocomplete(parser)
    return parser


def load_logger():
    '''
    Function to define the program logging object.
    '''

    logging.addLevelName(logging.INFO, "[\033[36mINFO\033[0m]")
    logging.addLevelName(logging.ERROR, "[\033[31mERROR\033[0m]")
    logging.addLevelName(logging.DEBUG, "[\033[32mDEBUG\033[0m]")
    logging.addLevelName(logging.WARNING, "[\033[33mWARNING\033[0m]")
    logging.basicConfig(
        level=logging.INFO,
        format="  %(levelname)s %(message)s"
    )
    return logging.getLogger('main')
