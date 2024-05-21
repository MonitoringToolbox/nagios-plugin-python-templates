#!/usr/bin/env python

"""
Description.

This Nagios check script serves as a more sophisticated example that uses
utility functions to guarantee the accuracy of the output and exit code.

Unlike the basic version, this one utilizes command-line parameters to override
the default hard-coded values, thereby enabling more advanced or portable
scripting. Nevertheless, we also supply a basic version suitable for checks that
don't demand parameters.
"""

import argparse
import random   # Only required for the template demo - can be removed
import sys

from typing import NoReturn


def main(options: argparse.Namespace) -> NoReturn:
    """
    Provide a main function.

    This function is where you can include all the code related to the check.
    You're free to define additional functions and invoke them whenever necessary.

    In this template, we've generated a random number to illustrate how to call
    the core functions that manage the different states. However, real tests will
    be more intricate and elaborate, but they should adhere to the same fundamental
    structure.

    Arguments:
        options (argparse.Namespace) -- _description_

    Returns:
        NoReturn -- _description_
    """
    test_value: int = random.randint(1, 100)  # nosec B311

    if test_value >= options.critical_level:
        handle_critical(f"Test Value = {test_value}")
    elif test_value >= options.warning_level:
        handle_warning(f"Test Value = {test_value}")
    elif test_value >= 0:
        handle_ok(f"Test Value = {test_value}")
    else:
        handle_unknown(f"Test Value = {test_value}")


def process_arguments() -> argparse.Namespace:
    """
    Process Arguments.

    This function handles the input from the command line. In this template, we've
    included an illustration of how to retrieve and process fresh warning and
    critical values. All the inputs are stored in the 'options' hash and then passed
    on to main().

    You can add as many fresh inputs as your check requires.

    Returns:
        argparse.Namespace -- _description_
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--critical', help="Critical level", type=float, dest="critical_level", default=90)
    parser.add_argument('-w', '--warning', help="Warning level", type=float, dest="warning_level", default=75)

    options: argparse.Namespace = parser.parse_args()

    if options.warning_level >= options.critical_level:
        handle_unknown("Warn level MUST be lower than Critical level")

    main(options)

# -------------------------------------------------------------------------------- #
# STOP HERE!                                                                       #
# -------------------------------------------------------------------------------- #
# The functions listed below are integral to the template and do not necessitate   #
# any modifications to use this template. If you intend to make changes to the     #
# code beyond this point, please make certain that you comprehend the consequences #
# of those alterations!                                                            #
# -------------------------------------------------------------------------------- #


def handle_ok(message: str = '') -> NoReturn:
    """
    Handle OK.

    If provided with a message, this function will show it with the 'OK' prefix and
    subsequently terminate the script with the requisite exit code of 0.

    Arguments:
        message (str) -- _description_ (default: '')

    Returns:
        NoReturn -- _description_
    """
    if message.strip():
        print(f"OK - {message}")
    sys.exit(0)


def handle_warning(message: str = '') -> NoReturn:
    """
    Handle Warning.

    If provided with a message, this function will show it with the 'WARNING' prefix
    and subsequently terminate the script with the requisite exit code of 1.

    Arguments:
        message (str) -- _description_ (default: '')

    Returns:
        NoReturn -- _description_
    """
    if message.strip():
        print(f"WARNING - {message}")
    sys.exit(1)


def handle_critical(message: str = '') -> NoReturn:
    """
    Handle Critical.

    If provided with a message, this function will show it with the 'CRITICAL' prefix
    and subsequently terminate the script with the requisite exit code of 2.

    Arguments:
        message (str) -- _description_ (default: '')

    Returns:
        NoReturn -- _description_
    """
    if message.strip():
        print(f"CRITICAL - {message}")
    sys.exit(2)


def handle_unknown(message: str = '') -> NoReturn:
    """
    Handle Unknown.

    If provided with a message, this function will show it with the 'UNKNOWN' prefix
    and subsequently terminate the script with the requisite exit code of 3.

    Arguments:
        message (str) -- _description_ (default: '')

    Returns:
        NoReturn -- _description_
    """
    if message.strip():
        print(f"UNKNOWN - {message}")
    sys.exit(3)

# -------------------------------------------------------------------------------- #
# The Core                                                                         #
# -------------------------------------------------------------------------------- #
# This is the central component of the script.                                     #
# -------------------------------------------------------------------------------- #


if __name__ == "__main__":
    process_arguments()

# -------------------------------------------------------------------------------- #
# End of Script                                                                    #
# -------------------------------------------------------------------------------- #
# This is the end - nothing more to see here.                                      #
# -------------------------------------------------------------------------------- #
