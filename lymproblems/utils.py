import os
import sys
import subprocess


def system(cmd):
    """
    Runs a shell command, and returns the output, err, returncode
    :param cmd: The command to run.
    :return:  Tuple with (output, err, returncode).
    """
    ret = subprocess.Popen(
        cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True,
        universal_newlines=True,
    )
    out, err = ret.communicate()  # type: str, str
    returncode = ret.returncode
    return out, err, returncode


def success():
    print("\n\033[92mSuccess. Now try next problem.\033[0m")
    sys.exit(0)


def fail(msg="Failed"):
    print("\033[91m{}\033[0m".format(msg))
    sys.exit(1)


def find_path_data(path):
    "First verify that the path exists, and then return the data"
    if not os.path.exists(path):
        print("Missing: {0}".format(path))
        sys.exit(1)

    with open(path) as fobj:
        data = fobj.read()
    return data
