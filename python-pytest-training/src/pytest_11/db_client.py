# db_client.py

def connect_to_database(config):
    if config["type"] == "sqlite":
        print("1st case")
        return f"Connected to SQLite with database {config['database']}"
    elif config["type"] == "postgres":
        print("2nd case")
        return f"Connected to PostgreSQL with database {config['database']}"
    elif config["type"] == "mysql":
        print("3rd case")
        return f"Connected to MySQL with database {config['database']}"
    else:
        raise ValueError("Unsupported database type")
