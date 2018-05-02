import json


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
        self.number = kwargs.get('number', None)
        self.id = kwargs.get('id', None)
        self.title = kwargs.get('title', None)
        self.description = kwargs.get('description', None)
        self.severity = kwargs.get('severity', None)
        self.owner = kwargs.get('owner', None)
        self.start_date = kwargs.get('start_date', None)
        self.flag = kwargs.get('flag', False)
        self.tlp = kwargs.get('tlp', 2)
        self.resolution_status = kwargs.get('resolution_status', None)
        self.impact_status = kwargs.get('impact_status', None)
        self.summary = kwargs.get('summary', None)
        self.end_date = kwargs.get('end_date', None)
        self.status = kwargs.get('status', 'Open')
        self.merge_into = kwargs.get('merge_into', None)
        self.merge_from = kwargs.get('merge_from', None)

        self.reports = kwargs.get('reports', {})
        self.metrics = kwargs.get('metrics', {})
        self.custom_fields = kwargs.get('customFields', {})

        tags = kwargs.get('tags', [])
        if not isinstance(tags, list):
            self.tags = [tags]
        else:
            self.tags = tags

        # observables = kwargs.get('observables', [])
        # if not isinstance(observables, list):
        #     self.observables = [observables]
        # else:
        #     self.observables = observables
        #
        # tasks = kwargs.get('tasks', None)
        # if not isinstance(tasks, list):
        #     self.tasks = [tasks]
        # else:
        #     self.tasks = tasks

    def __str__(self):
        return json.dumps(self.__dict__, indent=2)

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
        if self.number != case.number:
            diff.append('number')
        if self.id != case.id:
            diff.append('id')
        if self.title != case.title:
            diff.append('title')
        if self.description != case.description:
            diff.append('description')
        if self.severity != case.severity:
            diff.append('severity')
        if self.owner != case.owner:
            diff.append('owner')
        if self.start_date != case.start_date:
            diff.append('start_date')
        if self.flag != case.flag:
            diff.append('flag')
        if self.tlp != case.tlp:
            diff.append('tlp')
        if self.resolution_status != case.resolution_status:
            diff.append('resolution_status')
        if self.impact_status != case.impact_status:
            diff.append('impact_status')
        # Todo: add missing attribute checks
        return diff
