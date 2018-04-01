class Case(object):
    """This represents a TheHive case."""
    def __init__(self, **kwargs):
        """This is just a skeleton defining some variables that might be useful for the case model."""
        self.case_number = None
        self.case_id = None
        self.case_title = None
        self.case_description = None

        self.case_observables = list()
        self.case_tasks = list()

        self.case_owner = None