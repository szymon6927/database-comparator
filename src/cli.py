SUPPORTED_DATABASES_CLI_ARGS = ['mysql', 'postgresql']


def is_valid_database_cli_arg(arg: str):
    return arg in SUPPORTED_DATABASES_CLI_ARGS
