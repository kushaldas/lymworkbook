# The user will install Rust programming language following steps from
# <https://rustup.rs>, and then update the `PATH` variable in such a way so that
# **rustc** is available. 

import os
import sys
from .utils import system, success, fail


def setup():
    "Setup problemname"
    pass  # Nothing to do.


def verify():
    "Verify installrust"
    out, err, return_code = system('which rustc')

    if return_code != 0 and out.endswith(".cargo/bin/rustc"):
        fail("Can not find **rustc** in the right path.")
    # if everything okay, then
    success()
