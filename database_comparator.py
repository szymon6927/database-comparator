import sys

import click

from src.cli import is_valid_database_cli_arg
from src.core.enums import DBEnum
from src.core.factory import MultipleDatabaseTypeFactory


@click.command()
@click.option('--database', '-db', help='database type which you want to test')
@click.option('--operations-number', '-opn', default=10, help='number of operations performed on the database')
@click.option('--draw', help='use this flag if you want to draw a chart with the results', is_flag=True)
def main(database, operations_number, draw):
    """
    Database Comparator - Netguru RnD project
    The goal of the project is to make a database comparison.
    In order to be able to make this maintainable we use pure CQRS pattern.
    Supported databases:
    - MySQL
    """

    print('Welcome in Database Comparator (Netguru RnD project) ✨')

    if not is_valid_database_cli_arg(database):
        sys.exit(f'ERROR! database argument is not valid - possible choices {DBEnum.list()}')

    database_test_factory = MultipleDatabaseTypeFactory()
    database_test = database_test_factory.create_database_test(database, operations_number)
    database_test.present_results(draw)


if __name__ == '__main__':
    main()
