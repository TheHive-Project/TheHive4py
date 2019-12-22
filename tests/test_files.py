"""Test what happens when we try to attach files to things."""
try:
    import mock
except ImportError:
    import unittest.mock as mock

import thehive4py.models
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable


@mock.patch('thehive4py.api.requests.post')
def test_file_observable_named_file(mock_post):
    thehive = TheHiveApi('http://127.0.0.1:9000', 'API_KEY')
    test_id = 'AV55EOIsPQ_zDQrlj4a9'
    with mock.patch('thehive4py.models.open', mock.mock_open()):
        file_observable = CaseObservable(dataType='file',
                                         data=['pic.png'],
                                         tlp=1,
                                         ioc=True,
                                         tags=['thehive4py'],
                                         message='test')
        response = thehive.create_case_observable(test_id, file_observable)
        # if we just pass in the filename, the file has to be opened ...
        assert thehive4py.models.open.call_count > 0
        # ... but it can't be closed in this scope - this is the problem of #10
        # assert thehive4py.models.open.return_value.close.call_count == thehive4py.models.open.call_count
    assert mock_post.call_count == 1


