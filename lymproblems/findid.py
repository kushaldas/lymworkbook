# Find your user id and write it down in a file `/tmp/myuserid.txt`.

import os
import sys
from .utils import system, success, find_path_data

def setup():
    "Setup findid"
    pass  # Nothing to do.

def verify():
    "Verify findid"
    data = find_path_data('/tmp/myuserid.txt')
    if data.strip() != "1000":
        print("Your standard vagrant user id is supposed to be 1000.")
        sys.exit(1)
    # if everything okay, then
    success()
