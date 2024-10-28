from unittest.mock import patch, Mock
from pytest_6.my_api_client import fetch_data_from_api


@patch('pytest_6.my_api_client.requests.get')
def test_fetch_data_from_api(mock_get):
    fake_response = Mock()
    fake_response.json.return_value = {"key" : "value"}

    mock_get.return_value = fake_response

    url = "http://fakeapi.com/data"
    result = fetch_data_from_api(url)

    mock_get.assert_called_once_with(url)  # Check if requests.get was called with the correct URL
    assert result == {"key": "value"}