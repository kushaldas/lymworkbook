# Read the file at `/etc/os-release` and write the value of ID_LIKE (without the
# double quotes) in a file at `/tmp/id_like.txt`.

import os
import sys
from .utils import system, success

def setup():
    "Setup basicvim"
    pass  # Nothing to do.

def verify():
    "Verify basicvim"
    filename = '/tmp/id_like.txt'
    if not os.path.exists(filename):
        print("Output file is missing.")
        sys.exit(1)
    with open(filename) as fobj:
        data = fobj.read()

    if "rhel fedora" != data.strip():
        print("Wrong data in the output file.")
        sys.exit(1)
    success()