# database-comparator


![](https://img.shields.io/badge/code%20style-black-black)
![](https://img.shields.io/badge/code%20style-flake8-lightgrey)
![](https://img.shields.io/badge/code%20style-isort-blue)
![](https://img.shields.io/badge/tool-pre--commit-yellow)

![](https://img.shields.io/github/languages/count/szymon6927/database-comparator)
![](https://img.shields.io/github/languages/top/szymon6927/database-comparator)
![](https://img.shields.io/github/issues-pr/szymon6927/database-comparator)
![](https://img.shields.io/github/stars/szymon6927/database-comparator?style=social)


Python Netguru RnD - Database comparator

The goal of the project is to make a database comparison.
In MVP it may be just two, maybe three databases (PostgreSQL, MySQL, MongoDB).
In order to be able to make this maintainable we should use pure CQRS pattern.


## Stack

- Python 3.7
- Docker & Docker Compose


## Prerequisites

Make sure you have installed all of the following prerequisites on your development machine:

- [GIT](https://git-scm.com/downloads)
- [Make](http://gnuwin32.sourceforge.net/packages/make.htm)
- [Python 3.7](https://www.python.org/downloads/)
- [Docker version >= 19.03.1](https://www.docker.com/get-started)
- [docker-compose version >= 1.24.1](https://docs.docker.com/compose/install/)


## Local development

Create a virtual environment
```
$ python3 -m venv venv
```

Run a virtualenv environment
```
$ source venv/bin/activate
```

Install required packages with dev dependencies
```
$ pip install -r requirements/dev.txt
```

Create `config.env` file by copying `config.env.tmp` and fill these with required environment variables

Export local environment variables

On Mac OS
```bash
$ set -o allexport; source config.env; set +o allexport;
```

Then
```bash
$ docker-composue -up -d
```

If all of the containers are running:
```bash
$ docker exec -i mysql_database mysql -u$MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE < fixtures/mysql_schema.sql
$ docker exec -i mysql_test_database mysql -u$MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE < fixtures/mysql_schema.sql

$ docker cp ./fixtures/postgresql_schema.sql postgres_database:/postgresql_schema.sql
$ docker exec -i postgres_database psql -h$POSTGRES_HOST -d$POSTGRES_DB -U$POSTGRES_USER -p$POSTGRES_PORT -a -w -f postgresql_schema.sql

$ docker cp ./fixtures/postgresql_schema.sql postgres_test_database:/postgresql_schema.sql
$ docker exec -i postgres_test_database psql -h$POSTGRES_HOST -d$POSTGRES_DB -U$POSTGRES_USER -p$POSTGRES_PORT -a -w -f postgresql_schema.sql
```


## CLI

General overview
```
$ python3 database_comparator.py --help

Usage: database_comparator.py [OPTIONS]

  Database Comparator - Netguru RnD project The goal of the project is to
  make a database comparison. In order to be able to make this maintainable
  we use pure CQRS pattern.

  Supported databases: MySQL, PostgreSQL, MongoDB

Options:
  -db, --database TEXT            database type which you want to test,
                                  supported args: ['mysql', 'postgresql',
                                  'mongo']
  -opn, --operations-number INTEGER
                                  number of operations performed on the
                                  database
  --draw                          use this flag if you want to draw a chart
                                  with the results
  --help                          Show this message and exit.
```

Example usage:
```bash
$ python3 -db mysql -opn 100
```

Default operations number is `10` so
```bash
$ python3 -db mysql
```
will perform 10 operations on the database

If you want to draw a bar chart with the performance test results use `--draw` flag eg.
```
$ python3 -db mongo -opn 100 --draw
```

## Env variables

All required env variables are in `config.env.tmp` file


## Tests

If you want to run the tests then in root app directory type:
```
pytest -v
```

or
```
make run-tests
```

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

If you want to run the tests type:
```
$ make run-tests
```


## Git flow

Create your feature branch from master.

Branch naming:
- pattern: jira-task-id-short-description
- eg: BN-20-add-mongo-driver

Commit names conventions:
- pattern. [jira-task-id]: commit description
- eg. [BN-20]: Added delete CQRS command for mongo driver

After finishing implementation of your feature - create pull request to master branch.


## Troubleshooting



### Authors

Szymon Miks
