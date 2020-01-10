SUPPORTED_DATABASES_CLI_ARGS = ['mysql']


def is_valid_database_cli_arg(arg: str):
    return arg in SUPPORTED_DATABASES_CLI_ARGS
