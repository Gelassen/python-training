# test_db_client.py

import pytest
from db_client import connect_to_database

# Parameterized fixture
@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def db_config(request):
    if request.param == "sqlite":
        return {"type": "sqlite", "database": "test.db"}
    elif request.param == "postgres":
        return {"type": "postgres", "database": "test_pg"}
    elif request.param == "mysql":
        return {"type": "mysql", "database": "test_mysql"}
    else:
        raise ValueError("Unknown database type")

# Indirect parameterization of db_config
@pytest.mark.parametrize("db_config", ["sqlite", "postgres", "mysql"], indirect=True)
def test_connect_to_database(db_config):
    result = connect_to_database(db_config)
    
    # Assert the function returns the expected result based on config
    assert f"Connected to {db_config['type'].capitalize()}".lower()  in result.lower() 
    assert f"database {db_config['database']}".lower()  in result.lower() 