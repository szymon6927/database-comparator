from unittest.mock import patch

import pytest
from click.testing import CliRunner

from database_comparator import main
from src.core.enums import DBEnum


@pytest.mark.parametrize('db_type', DBEnum.list())
@patch('src.core.factory.MultipleDatabaseTypeFactory.create_database_test')
def test_cli_database_option_with_default_operation_number(mock_create_database_test, db_type):
    default_operation_number = 10

    runner = CliRunner()
    result = runner.invoke(main, ['--database', db_type])

    mock_create_database_test.assert_called_with(db_type, default_operation_number)

    assert result.exit_code == 0


def test_cli_database_option_incorrect_db_type():
    runner = CliRunner()
    result = runner.invoke(main, ['--database', 'test'])

    assert result.exit_code != 0


@pytest.mark.parametrize('db_type', DBEnum.list())
@patch('src.core.factory.MultipleDatabaseTypeFactory.create_database_test')
def test_cli_database_option_with_operation_number(mock_create_database_test, db_type):
    operation_number = 100

    runner = CliRunner()
    result = runner.invoke(main, ['--database', db_type, '--operations-number', operation_number])

    mock_create_database_test.assert_called_with(db_type, operation_number)

    assert result.exit_code == 0
