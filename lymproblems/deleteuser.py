# Remove the fatima user from the system

import os
import sys
from .utils import system, success, fail, find_path_data

def setup():
    "Setup problemname"
    pass  # Nothing to do.

def verify():
    "Verify newuser"
    data = find_path_data("/etc/passwd")
    lines = data.split()
    flag = False
    for line in lines:
        if line.startswith("fatima"):
            flag = True
    
    if flag:
        fail("User fatima is still there.")
    # if everything okay, then
    success()