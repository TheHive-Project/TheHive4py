from unittest import mock

from thehive4py.api import TheHiveApi


@mock.patch('thehive4py.api.requests.get')
def test_get_case(mock_get):
    thehive = TheHiveApi('http://127.0.0.1:9000', 'username', 'password', {'http': '', 'https': ''})

    test_id = 'AV55EOIsPQ_zDQrlj4a9'
    test_json = {
        '_type': 'case',
        'caseId': 5,
        'createdAt': 1505269703195,
        'createdBy': 'username',
        'customFields': {},
        'description': 'test description',
        'flag': False,
        'id': test_id,
        'metrics': {},
        'owner': 'username',
        'severity': 2,
        'startDate': 1505269703000,
        'status': 'Open',
        'tags': [],
        'title': 'test case',
        'tlp': 2,
        'user': 'username'
    }

    mock_response = mock.Mock()
    mock_response.json.return_value = test_json
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    case = thehive.case(test_id)

    assert mock_response.json.call_count == 1
    assert case.id == test_id

