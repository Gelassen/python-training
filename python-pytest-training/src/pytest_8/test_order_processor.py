from unittest.mock import patch
from pytest_8.user_service import UserService
from pytest_8.inventory_service import InventoryService
from pytest_8.order_processor import process_order

def test_order_processor():
    mock_user_service_response = {"data": "mocked data"}
    mock_inventory_service_response = {"inventoryCount": "42"}

    # Provide the full path to the methods you are patching, as strings
    with patch('pytest_8.user_service.UserService.get_user_by_id', return_value=mock_user_service_response), \
         patch('pytest_8.inventory_service.InventoryService.check_stock', return_value=mock_inventory_service_response):

        # Call the function being tested
        result = process_order(40012)

        # Assert that the response matches the expected mock data
        assert result == mock_inventory_service_response
