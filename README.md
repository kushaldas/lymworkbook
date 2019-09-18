## Work for the LYM book

This is a fresh workbook for the LYM readers. This is using Vagrant to build up the vm, you can 
actually use it in a normal vm too. Make sure that you have a `vagrant` user and you can ssh into
the vm from your normal work computer. Also, this user should be able to do `sudo` without password.

## TODO (Add steps for the above mentioned things)


## How to use the tool?

First you will get the vm ready.

```
vagrant up
vagrant ssh workbook
```

Next, to create any of the problems, type `sudo lymsetup PROMBLEM_NAME` command.

```
sudo lymsetup copypaste
```

To verify your work, type `sudo lymverify PROBLEM_NAME` command.

```
sudo lymverify copypaste
```

If you managed to solve the problem, you will see the following output.

```
Success. Now try next problem.
```


## Template of a new problem

```Python

# A small paragraph explaining the problem.
# This has to be updated if there is any change in the
# problem statement.

import os
import sys
from .utils import system, success, fail, find_path_data

def setup():
    "Setup problemname"
    pass  # Nothing to do.

def verify():
    "Verify problemname"
    pass
    # if everything okay, then
    success()
    # If something is not correct then
    fail("You failed to setup xyz")

```

Fill in the `setup` and `verify` functions. Remember to use
[black](https://pypi.org/project/black/) on the code before you submit a PR.

## License: GPLv3+
