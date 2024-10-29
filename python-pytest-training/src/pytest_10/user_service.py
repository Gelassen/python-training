# user_service.py
import requests

def get_user_data(user_id):
    response = requests.get(f"http://example.com/users/{user_id}")
    return response.json()
