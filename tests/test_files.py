"""Test what happens when we try to attach files to things."""
try:
    import mock
except ImportError:
    import unittest.mock as mock

import thehive4py.models
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable
from io import StringIO

@mock.patch('thehive4py.api.requests.post')
def test_file_observable_named_file(mock_post):
    thehive = TheHiveApi('http://127.0.0.1:9000', 'API_KEY')
    test_id = 'AV55EOIsPQ_zDQrlj4a9'
    with mock.patch('thehive4py.models.open', mock.mock_open()):
        file_observable = CaseObservable(dataType='file',
                                         data='pic.png',
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

@mock.patch('thehive4py.api.requests.post')
def test_file_observable_file_object(mock_post):
    thehive = TheHiveApi('http://127.0.0.1:9000', 'API_KEY')
    test_id = 'AV55EOIsPQ_zDQrlj4a9'
    our_file = mock.Mock(wraps=StringIO(u'contents of file'))
    with mock.patch('thehive4py.models.open', mock.mock_open()):
        file_observable = CaseObservable(dataType='file',
                                         data=(our_file, 'pic.png'),
                                         tlp=1,
                                         ioc=True,
                                         tags=['thehive4py'],
                                         message='test')
        response = thehive.create_case_observable(test_id, file_observable)
        # if we pass in the file object, it does not have to be opened ...
        assert thehive4py.models.open.call_count == 0
        # ... operations happen on our file ...
        assert our_file.read.call_count > 0
        assert our_file.seek.call_count > 0
        # ... and balance between opens and closes is achieved
        assert thehive4py.models.open.return_value.close.call_count == thehive4py.models.open.call_count
        assert our_file.close.call_count == 0
    assert mock_post.call_count == 1


