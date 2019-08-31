import os
import sys
import importlib


def find_module():
    if len(sys.argv) != 2:
        print("Missing problem name.")
        sys.exit(1)

    # Now setup the problem
    name = "lymproblems." + sys.argv[1]
    try:
        module = importlib.import_module(name)
    except ImportError:
        print("No such defined problem: {0}".format(sys.argv[1]))
        print("Please check for any typo in the problem name.")
        sys.exit(1)
    return module


def workbook_setup():
    module = find_module()
    module.setup()


def workbook_verify():
    module = find_module()
    module.verify()
