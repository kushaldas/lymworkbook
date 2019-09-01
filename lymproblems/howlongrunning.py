# Which command to use to find out how long the computer is running?

import os
import sys
from .utils import system, success, fail


def setup():
    "Setup dns1"
    pass  # Nothing to do.


def verify():
    "Verify dns1"
    cmd = raw_input("Enter the command: ")
    cmd = cmd.strip()
    if cmd == "uptime":
        success()

    fail("Wrong command")
