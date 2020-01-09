# database-comparator
Python Netguru RnD - Database comparator

## Pre-commit config

We use a pre-commit hook which checking a quality of code.
To install a hook on your local repository, you have to run a command given below, after install required packages:

```
$ pre-commit install
```

## Makefile

We use Makefile to automate some common stuff

If you want to update dependencies type:
```
$ make update-deps
```

If you want to format code type:
```
$ make format
```
