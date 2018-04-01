class Observable(object):
    """This represents a TheHive observable"""
    def __init__(self, **kwargs):
        """"""
        self.observable_data = kwargs.get('observable_data', None)
        self.observable_attachment = kwargs.get('observable_attachment', None)
        self.observable_type = kwargs.get('observable_type')
        self.observable_message = kwargs.get('observable_message', None)
        self.observable_tlp = kwargs.get('observable_tlp', 2)
        self.observable_ioc = kwargs.get('observable_ioc', False)
        self.observable_status = kwargs.get('observable_status', 'Ok')

        tags = kwargs.get('observable_tags', [])
        if not isinstance(tags, list):
            self.observable_tags = [tags]
        else:
            self.observable_tags = tags

        # Check if either data or attachment is given
        if not self.observable_data and not self.observable_attachment:
            raise ValueError('Either data or attachment attribute must be filled.')
