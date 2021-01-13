class TheHiveException(Exception):
    """
    Base class for TheHive exceptions
    """
    pass


class CaseException(TheHiveException):
    """
    Exception raised by failure of API calls related to `Case` handling
    """
    pass


class CaseTaskException(CaseException):
    """
    Exception raised by failure of API calls related to `Case Task` handling
    """
    pass


class CaseTaskLogException(CaseTaskException):
    """
    Exception raised by failure of API calls related to `Case Task Log` handling
    """
    pass


class CaseObservableException(CaseException):
    """
    Exception raised by failure of API calls related to `Case Observable` handling
    """
    pass


class ObservableException(TheHiveException):
    """
    Exception raised by failure of API calls related to `Observable` handling
    """
    pass


class AlertException(TheHiveException):
    """
    Exception raised by failure of API calls related to `Alert` handling
    """
    pass


class AlertArtifactException(CaseException):
    """
    Exception raised by failure of API calls related to `Alert Artifact` handling
    """
    pass


class CaseTemplateException(TheHiveException):
    """
    Exception raised by failure of API calls related to `Case Template` handling
    """
    pass


class CustomFieldException(TheHiveException):
    """
    Exception raised by failure of API calls related to `Custom Fields` handling
    """
    pass
