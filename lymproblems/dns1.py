# Use 1.1.1.1 as DNS resolver of the sytem

import os
import sys
from .utils import system, success, failure

def setup():
    "Setup dns1"
    pass  # Nothing to do.

def verify():
    "Verify dns1"
    data = ""
    with open('/etc/resolv.conf') as f:
        data = f.readlines()

    for line in data:
        line = line.strip()
        words = line.split()
        if len(words) == 2:
            if words[0] == "nameserver" and words[1] == "1.1.1.1":
                success()
    

    failure("Can not find correct DNS entry")
    
    