# Create a new RSA ssh key (with passphrase) for the vagrant user

import os
import sys
import getpass
import paramiko

from .utils import system, success, fail, find_path_data


def setup():
    "Setup newrsakey"
    pass  # Nothing to do.


def verify():
    private_key_path = os.path.join(os.path.expanduser("~"), ".ssh/id_rsa")
    if not os.path.exists(private_key_path):
        fail("Private key is missing.")

    password = getpass.getpass("Enter the password for the ssh key:")
    try:
        key = paramiko.RSAKey.from_private_key_file(private_key_path, password)
    except paramiko.ssh_exception.SSHException:
        fail("Wrong password for the ssh key.")
    success()
