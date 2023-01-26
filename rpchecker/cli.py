"""Provide several command line interface for the application.

The module contains the following functions:
- `read_user_cli_args()` - Returns a namespace object containing the parsed arguments gotten
from command line.
- `display_check_result(result:bool, url:str, error="")` - Display the checking result

"""

import argparse

def read_user_cli_args() -> any:
    """ Handle the CLI argumemnts and options

    Examples:
        Can not give you example due to my stupid head

    Returns:
        A Namespace object containing the parsed arguments.

    """
    parser = argparse.ArgumentParser(
        prog = "rpchecker", description= "check the availability of websites"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar = "URLs", # 'metavar' sets a name for the argument in usage or help messages.
        nargs = "+", # 'nargs' tells argparse to accept a list of command-line arguments after the -u or --urls switch.
        type = str,
        default = [],
        help = "enter one or more website URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar = "FILE",
        type = str,
        default = "",
        help = "read URLs from a file",

    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously",
    )
    RESULT: any = parser.parse_args()
    return RESULT


def display_check_result(result:bool, url:str, error="") -> None:
    """Display the result of a connectivity check.

    Examples:
        Can not give you example because it's not necessary.

    Args:
        result: the site connectivity
        url: a website address
        error: the error info (if there is a crash)

    """
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Error: "{error}"')