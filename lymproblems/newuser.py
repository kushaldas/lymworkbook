# Add a new user called fatima to the system.


import os
import sys
from .utils import system, success, fail, find_path_data


def setup():
    "Setup newuser"
    pass  # Nothing to do.


def verify():
    "Verify newuser"
    data = find_path_data("/etc/passwd")
    lines = data.split()
    flag = False
    for line in lines:
        if line.startswith("fatima"):
            flag = True

    if not flag:
        fail("Missing user fatima.")
    # if everything okay, then
    success()
