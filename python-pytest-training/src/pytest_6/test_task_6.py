# test_api_client.py

import pytest
from unittest.mock import AsyncMock, patch, Mock
from src.pytest_6.api_client import fetch_data_from_api
from src.pytest_6.async_api_client import async_fetch_data_from_api

# test_async_api_client.py

@pytest.mark.asyncio
async def test_async_fetch_data_from_api():
    # Define fake response data
    fake_response_data = {"key": "value"}

    # Patch aiohttp.ClientSession
    with patch('aiohttp.ClientSession') as MockClientSession:
        # Create a mock instance of ClientSession
        mock_session = MockClientSession.return_value
        
        # Mock the get method to return an async context manager
        mock_get = mock_session.get
        
        # Create an AsyncMock for the response object
        mock_response = AsyncMock()
        mock_response.__aenter__.return_value = mock_response
        mock_response.__aexit__.return_value = None
        mock_response.json.return_value = fake_response_data
        
        # Set the mock get method to return our mock response
        mock_get.return_value = mock_response

        # Call the function under test
        url = "https://example.com/api/data"
        response = await async_fetch_data_from_api(url)

        # Assert that the mocked get method was called with the correct URL
        mock_get.assert_called_once_with(url)

        # Assert that the function returns the fake data we set up
        assert response == fake_response_data


def test_fetch_data_from_api():
    # Define a fake response data
    fake_response_data = {"key": "value"}

    # Use patch to mock requests.get method
    with patch('requests.get') as mock_get:
        # Set up the mock to return a response with our fake data
        mock_response = Mock()
        mock_response.json.return_value = fake_response_data
        mock_get.return_value = mock_response

        # Call the function under test
        url = "https://example.com/api/data"
        response = fetch_data_from_api(url)

        # Assert that the mocked method was called with the correct URL
        mock_get.assert_called_once_with(url)

        # Assert that the function returns the fake data we set up
        assert response == fake_response_data


# test_async_api_client.py
# @pytest.mark.asyncio
# async def test_fetch_data_from_api():
#     # Define a fake response data
#     fake_response_data = {"key": "value"}

#     # Mock the session and get method in aiohttp
#     with patch('aiohttp.ClientSession.get', new_callable=AsyncMock) as mock_get:
#         # Setup mock to return a response with our fake data
#         mock_response = AsyncMock()
#         mock_response.json.return_value = fake_response_data
#         mock_get.return_value = mock_response

#         # Call the function under test
#         url = "https://example.com/api/data"
#         response = await fetch_data_from_api(url)

#         # Assert that the mocked method was called with the correct URL
#         mock_get.assert_called_once_with(url)

#         # Assert that the function returns the fake data we set up
#         assert response == fake_response_data

# @pytest.mark.asyncio
# async def test_fetch_data_from_api():
#     # Define fake response data
#     fake_response_data = {"key": "value"}

#     # Mock the aiohttp.ClientSession context manager and its methods
#     with patch('aiohttp.ClientSession') as MockClientSession:
#         # Create an instance mock of ClientSession
#         mock_session = MockClientSession.return_value
        
#         # Mock the get method to return an async context manager
#         mock_get = mock_session.get

#         mock_result = Mock()
#         mock_result.scalar.return_value = fake_response_data
#         # Setup mock response to act as an async context manager
#         mock_response = AsyncMock(return_value=mock_result)
#         mock_response.__aenter__.return_value = mock_response
#         mock_response.__aexit__.return_value = None
#         mock_response.json.return_value = fake_response_data
        
#         mock_get.return_value = mock_response

#         # Call the function under test
#         url = "https://example.com/api/data"
#         response = await fetch_data_from_api(url)

#         # Assert that the mocked method was called with the correct URL
#         mock_get.assert_called_once_with(url)

#         # Assert that the function returns the fake data we set up
#         assert response == fake_response_data

