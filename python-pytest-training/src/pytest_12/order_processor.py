# order_processor.py
from user_service import UserService
from inventory_service import InventoryService

def process_order(user_id, product_id, quantity):
    user_data = UserService().get_user_by_id(user_id)
    stock_info = InventoryService().check_stock(product_id, quantity)

    if not user_data:
        raise ValueError("User not found")

    if stock_info["available"] < quantity:
        raise ValueError("Insufficient stock")

    # Assume some order processing logic here
    return {"status": "Order processed", "user": user_data, "stock": stock_info}
