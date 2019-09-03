# Add a new user `powerful` with `wheel` as the group for the user.

import os
import sys
from .utils import system, success, fail


def setup():
    "Setup usergroup"
    pass  # Nothing to do.


def verify():
    "Verify usergroup"
    flag = False
    with open('/etc/group') as fobj:
        for line in fobj:
            if line.startswith("wheel"):
                if line.find(":powerful") != -1:
                    flag = True

    if not flag:
        fail("Can not find `powerful` user in the `wheel` group.")
    # if everything okay, then
    success()
