import os
import sys
import subprocess

def system(cmd):
    """
    Runs a shell command, and returns the output, err, returncode
    :param cmd: The command to run.
    :return:  Tuple with (output, err, returncode).
    """
    ret = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True, universal_newlines=True)
    out, err = ret.communicate() # type: str, str
    returncode = ret.returncode
    return out, err, returncode

def success():
    print("\nSuccess. Now try next problem.")


def find_path_data(path):
    "First verify that the path exists, and then return the data"
    if not os.path.exists(path):
        print("Missing: {0}".format(path))
        sys.exit(1)

    with open(path) as fobj:
        data = fobj.read()
    return data
