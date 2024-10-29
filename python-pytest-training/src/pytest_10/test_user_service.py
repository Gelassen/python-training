# test_user_service.py
from pytest_10.user_service import get_user_data

def test_get_user_data(mocker):
    # Mock `requests.get` to return a fake response
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mocker.patch("user_service.requests.get", return_value=mock_response)

    # Call the function and assert the mocked result
    result = get_user_data(1)
    assert result == {"id": 1, "name": "John Doe"}
