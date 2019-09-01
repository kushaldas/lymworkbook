"""
Problem: 
1. Check if the /tmp/ip_dgplug.txt exits or not (if not found provide a feedback to the user).
2. Read the file and match if it is same of the ip_address you calculated below.
"""
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
            fail("The ip address is not same.")
        success()

    except socket.gaierror:
        fail("Please correct the site's URL. Either the URL is written incorrectly or the site itself is inaccessible.")
