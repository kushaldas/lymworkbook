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
python setup.py install
```

Next, to create any of the problems, type `lymsetup PROMBLEM_NUMBER` command.

```
lymsetup 1
```

To verify your work, type `lymverify PROBLEM_NUMBER` command.

```
lymverify 1
```

If you managed to solve the problem, you will see the following output.

```
Success. Now try next problem."
```


## License: GPLv3+