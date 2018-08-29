class TheHiveException(Exception):
    pass


class NotFoundError(TheHiveException):
    pass


class AuthenticationError(TheHiveException):
    pass


class AuthorizationError(TheHiveException):
    pass


class InvalidInputError(TheHiveException):
    pass


class ServiceUnavailableError(TheHiveException):
    pass


class ServerError(TheHiveException):
    pass


class CortexError(TheHiveException):
    pass