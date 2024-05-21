#!/usr/bin/env python

"""
Description.

The script presented here is a simple Nagios check example, employing a set of
utility functions to guarantee accurate output and exit codes. Although this
version uses fixed values, suitable for straightforward checks, we also offer a
more sophisticated variant that demonstrates how to handle command-line
arguments for more elaborate or flexible scripting.
"""

import random   # Only required for the template demo - can be removed
import sys

from typing import NoReturn


def main() -> NoReturn:
    """
    Define a summary.

    This function is where you can include all the code related to the check. You're
    free to define additional functions and invoke them whenever necessary.

    In this template, we've generated a random number to illustrate how to call the
    core functions that manage the different states. However, real tests will be
    more intricate and elaborate, but they should adhere to the same fundamental
    structure.

    Returns:
        NoReturn -- _description_
    """
    critical_level = 90
    warning_level = 75

    test_value: int = random.randint(1, 100)  # nosec B311

    if test_value >= critical_level:
        handle_critical(f"Test Value = {test_value}")
    elif test_value >= warning_level:
        handle_warning(f"Test Value = {test_value}")
    elif test_value >= 0:
        handle_ok(f"Test Value = {test_value}")
    else:
        handle_unknown(f"Test Value = {test_value}")

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

    Keyword Arguments:
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
    main()

# -------------------------------------------------------------------------------- #
# End of Script                                                                    #
# -------------------------------------------------------------------------------- #
# This is the end - nothing more to see here.                                      #
# -------------------------------------------------------------------------------- #
