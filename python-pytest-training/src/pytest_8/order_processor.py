import json

from pytest_8.inventory_service import InventoryService
from pytest_8.user_service import UserService

def process_order(order_id) -> json:
    print(f"UserService:: {UserService().get_user_by_id()}")
    
    return InventoryService().check_stock()