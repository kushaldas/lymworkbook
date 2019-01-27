## Work for the LYM book

This is a fresh workbook for the LYM readers. This is using Vagrant to build up the vm, you can 
actually use it in a normal vm too. Make sure that you have a `vagrant` user and you can ssh into
the vm from your normal work computer. Also, this user should be able to do `sudo` without password.

## TODO (Add steps for the above mentioned things)


## How to use the tool?

First you will have to install the tool.

```
vagrant up
vagrant ssh
cd lymworkbook
sudo python setup.py install
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
Success. Now try next problem."
```


## Template of a new problem

```Python

# A small paragraph explaining the problem.
# This has to be update if there is any change in the
# problem statement.

import os
import sys
from .utils import system, success, find_path_data

def setup():
    "Setup problemname"
    pass  # Nothing to do.

def verify():
    "Verify problemname"
    pass
    # if everything okay, then
    success()

```

Fill in the `setup` and `verify` functions.


## License: GPLv3+