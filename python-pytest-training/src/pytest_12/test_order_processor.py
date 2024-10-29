from unittest.mock import patch, Mock
from order_processor import process_order

def test_process_order(benchmark):
    # Mock response data
    mock_user_data = {"id": 1, "name": "John Doe", "email": "john@example.com"}
    mock_stock_info = {"product_id": 101, "available": 50}

    # Use patch to mock the UserService and InventoryService calls within process_order
    with patch("order_processor.UserService") as MockUserService, \
         patch("order_processor.InventoryService") as MockInventoryService:
        
        mocked_user_service_instance = Mock()
        mocked_user_service_instance.get_user_by_id.return_value = mock_user_data
        MockUserService.return_value = mocked_user_service_instance

        mocked_inventory_service_instance = Mock()
        mocked_inventory_service_instance.check_stock.return_value = mock_stock_info
        MockInventoryService.return_value = mocked_inventory_service_instance

        # result = process_order(user_id=1, product_id=101, quantity=2)
        # Run the benchmark
        result = benchmark(process_order(user_id=1, product_id=101, quantity=2))

        assert result == {
            "status": "Order processed",
            "user": mock_user_data,
            "stock": mock_stock_info
        }
        
        # Verify the mocked methods were called with expected arguments
        mocked_user_service_instance.get_user_by_id.assert_called_once_with(1)
        mocked_inventory_service_instance.check_stock.assert_called_once_with(101, 2)