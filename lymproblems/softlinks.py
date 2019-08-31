# Create a softlink called `docs` in your home directory which will point to
# `/usr/share/doc/` directory. Also create another softlink called `meomory` to
# the `/proc/meminfo` file.


import os
import sys
from .utils import system, success, fail


def setup():
    "Setup softlinks"
    pass  # Nothing to do.


def verify():
    docs = "/home/vagrant/docs"
    if not os.path.exists(docs):
        fail("docs softlink is missing")

    path = os.readlink(docs)
    if path != "/usr/share/doc":
        fail("Not a correct symlink in docs")

    memory = "/home/vagrant/memory"
    if not os.path.exists(memory):
        fail("memory softlink is missing")

    path = os.readlink(memory)
    if path != "/proc/meminfo":
        fail("Not a correct symlink in memory")

    success()
