# Create a directory called `work` in your home directory, and copy the file
# from `/tmp/problem1/work/files/hello.txt` into the newly created diretory.
# Remember to remove the `/tmp/problem1/work/files/hello.txt` file afterwards.
# Create a file called `/tmp/chapter1/allusers` and add all of the directory
# names under your home directory into that file.

import os
import sys
from .utils import system, success

def setup():
    "Setup problem 1"
    system("mkdir -p /tmp/problem1/work/files")
    system("chown -R vagrant.vagrant /tmp/problem1")
    with open("/tmp/problem1/work/files/hello.txt", "w") as fobj:
        fobj.write("Hello user.")


def verify():
    "verify problem 1"
    if os.path.exists("/tmp/problem1/work/files/hello.txt"):
        print("/tmp/problem1/work/files/hello.txt still exits.")
        sys.exit(1)

    if not os.path.exists("/home/vagrant/work/hello.txt"):
        print("hello.txt is missing from the work directory in your home.")
        sys.exit(1)

    with open("/home/vagrant/work/hello.txt") as fobj:
        data = fobj.read()
        if not data == "Hello user.":
            print("hello.txt is corrupted or has wrong data.")
            sys.exit(1)

    success()
