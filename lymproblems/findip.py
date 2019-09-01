# Find the IP address of dgplug.org and save it to /tmp/ip_dgplug.txt file.

import os
import sys
import socket
from .utils import system, success, fail, find_path_data

def setup():
    "Setup find_ip"
    pass  # Nothing to do.

def verify():
    try:
        "Verify find_ip"
        site_url="dgplug.org"
        # Check for file "ip_dgplug.txt" in "/tmp" directory.
        data = find_path_data("/tmp/ip_dgplug.txt")

        # Compare the ip address obtained with data.
        if data.strip()!=socket.gethostbyname(site_url):
            fail("The IP address is not same.")
        success()

    except socket.gaierror:
        fail("Please correct the site's URL. Either the URL is written incorrectly or the site itself is inaccessible.")
