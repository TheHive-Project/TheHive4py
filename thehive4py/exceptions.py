class TheHiveException(Exception):
    """Base class for TheHive exceptions"""
    pass


class CaseException(TheHiveException):
    pass

class CaseTaskException(CaseException):
    pass

class CaseObservableException(CaseException):
    pass

class AlertException(TheHiveException):
    pass

class CaseTemplateException(TheHiveException):
    pass
