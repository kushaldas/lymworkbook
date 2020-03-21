# Grant administrative(sudo) privileges to an existing normal user account "lym".

import os
import sys
from .utils import system, success, fail, find_path_data


def setup():
    "Setup assignsudo"
    pass  # Nothing to do.


def verify():
    "Verify assignsudo"
    user = "lym"

    if system("sudo -l -U {}".format(user))[2] != 0:
        fail("User {} is not allowed to run sudo commands.".format(user))
    success()
