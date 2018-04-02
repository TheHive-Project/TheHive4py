class Case(object):
    """This represents a TheHive case."""
    def __init__(self, **kwargs):
        """As this class can be used for creating a new case, too, case_number and case_id can be empty. So, through
        creating an instance, everything is optional and the attributes are checked in the specific api methods for
        creating or updating the class.

        :param case_number: Ascending case number visible in TheHive ui
        :param case_id: Elasticsearch document id of the case
        # Todo: Add the case fields to docstring
        """
        self.case_number = kwargs.get('case_number', None)
        self.case_id = kwargs.get('case_id', None)
        self.case_title = kwargs.get('case_title', None)
        self.case_description = kwargs.get('case_description', None)
        self.case_severity = kwargs.get('case_severity', None)
        self.case_owner = kwargs.get('case_owner', None)
        self.case_start_date = kwargs.get('case_start_date', None)
        self.case_flag = kwargs.get('case_flag', False)
        self.case_tlp = kwargs.get('case_tlp', 2)
        self.case_resolution_status = kwargs.get('case_resolution_status', None)
        self.case_impact_status = kwargs.get('case_impact_status', None)
        self.case_summary = kwargs.get('case_summary', None)
        self.case_end_date = kwargs.get('case_end_date', None)
        self.case_status = kwargs.get('case_status', 'Open')
        self.case_merge_into = kwargs.get('case_merge_into', None)
        self.case_merge_from = kwargs.get('case_merge_from', None)

        metrics = kwargs.get('case_metrics', [])
        if not isinstance(metrics, list):
            self.case_metrics = [metrics]
        else:
            self.case_metrics = metrics

        tags = kwargs.get('case_tags', [])
        if not isinstance(tags, list):
            self.case_tags = [tags]
        else:
            self.case_tags = tags

        observables = kwargs.get('case_observables', [])
        if not isinstance(observables, list):
            self.case_observables = [observables]
        else:
            self.case_observables = observables

        tasks = kwargs.get('case_tasks', None)
        if not isinstance(tasks, list):
            self.case_tasks = [tasks]
        else:
            self.case_tasks = tasks

    @staticmethod
    def from_json(**kwargs):
        return Case(
            # Todo: Add case fields from TH case object
        )

    def diff(self, case):
        """Returns a list of attributes that are different between the two cases compared. Can be used e.g. for updating
        attributes of cases over the api."""
        if not isinstance(case, Case):
            raise TypeError('case should be of type Case.')

        diff = []
        if self.case_number != case.case_number:
            diff.append('case_number')
        if self.case_id != case.case_id:
            diff.append('case_id')
        if self.case_title != case.case_title:
            diff.append('case_title')
        if self.case_description != case.case_description:
            diff.append('case_description')
        if self.case_severity != case.case_severity:
            diff.append('case_severity')
        if self.case_owner != case.case_owner:
            diff.append('case_owner')
        if self.case_start_date != case.case_start_date:
            diff.append('case_start_date')
        if self.case_flag != case.case_flag:
            diff.append('case_flag')
        if self.case_tlp != case.case_tlp:
            diff.append('case_tlp')
        if self.case_resolution_status != case.case_resolution_status:
            diff.append('case_resolution_status')
        if self.case_impact_status != case.case_impact_status:
            diff.append('case_impact_status')
        # Todo: add missing attribute checks
        return diff
