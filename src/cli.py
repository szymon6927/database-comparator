from src.core.enums import DBEnum


def is_valid_database_cli_arg(arg: str):
    return arg in DBEnum.list()
