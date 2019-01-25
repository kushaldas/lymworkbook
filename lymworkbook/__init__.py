import os
import sys

import problem1

PROBLEMS = {}
PROBLEMS["problem1"] = problem1

def workbook_setup():
    if len(sys.argv) != 2:
        print("Missing problem number.")
        sys.exit(1)

    # Now setup the problem
    name = "problem" + sys.argv[1]
    PROBLEMS[name].setup()


def workbook_verify():
    if len(sys.argv) != 2:
        print("Missing problem number.")
        sys.exit(1)

    # Now setup the problem
    name = "problem" + sys.argv[1]
    PROBLEMS[name].verify()