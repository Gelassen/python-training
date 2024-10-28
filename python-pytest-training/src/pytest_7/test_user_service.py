from unittest.mock import patch
from pytest_7.user_service import UserService

def test_get_user_by_id():
    mock_user = {"id": 1, "name": "Alice", "email": "alice@example.com"}

    with patch.object(UserService, 'get_user_by_id', return_value=mock_user):
        service = UserService()
        user = service.get_user_by_id(1)

        assert user == mock_user