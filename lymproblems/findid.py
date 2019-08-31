# Find your user id and write it down in a file `/tmp/myuserid.txt`.

import os
import sys
from .utils import system, success, fail, find_path_data

def setup():
    "Setup findid"
    pass  # Nothing to do.

def verify():
    "Verify findid"
    data = find_path_data('/tmp/myuserid.txt')
    if data.strip() != "1000":
        fail("Your standard vagrant user id is supposed to be 1000.")
    # if everything okay, then
    success()
