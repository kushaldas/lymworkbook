# Create a softlink called `docs` in your home directory which will point to
# `/usr/share/doc/` directory. Also create another softlink called `meomory` to
# the `/proc/meminfo` file.


import os
import sys
from .utils import system, success

def setup():
    "Setup softlinks"
    pass  # Nothing to do.

def verify():
    docs = "/home/vagrant/docs"
    if not os.path.exists(docs):
        print("docs softlink is missing")
        sys.exit(1)

    path = os.readlink(docs)
    if path != "/usr/share/doc":
        print("Not a correct symlink in docs")
        sys.exit(1)

    memory = "/home/vagrant/memory"
    if not os.path.exists(memory):
        print("memory softlink is missing")
        sys.exit(1)

    path = os.readlink(memory)
    if path != "/proc/meminfo":
        print("Not a correct symlink in memory")
        sys.exit(1)

    success()
