# Change the system's timezone to the same of SFO, USA

import os
import sys
from .utils import system, success, fail


def setup():
    "Setup timezonechange"
    pass  # Nothing to do.


def verify():
    "Verify timezonechange"

    if os.path.realpath("/etc/localtime") != os.path.realpath(
        "/usr/share/zoneinfo/US/Pacific"
    ):
        fail("Time zone not changed")
    success()
