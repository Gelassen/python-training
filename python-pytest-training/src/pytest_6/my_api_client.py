import requests

def fetch_data_from_api(url):
    """
    Fetch data from the given URL using an HTTP GET request.
    
    :param url: URL of the API endpoint
    :return: JSON response from the GET request
    """
    response = requests.get(url)
    return response.json()  # Assuming the response is in JSON format
