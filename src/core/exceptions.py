class MissingEnvVariableError(Exception):
    """raise when env variable is not set"""

    pass


class NotExists(Exception):
    """raise when object not exist"""

    pass


class IllegalArgumentError(Exception):
    pass
