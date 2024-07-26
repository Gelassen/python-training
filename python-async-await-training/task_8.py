"""
    Database Access:
        Use an async database client (like asyncpg for PostgreSQL) to perform 
        asynchronous database operations such as inserting, updating, and 
        querying records.
"""

import asyncio
import asyncpg

async def insert_user(conn, name, age):
    await conn.execute('''
        INSERT INTO users(name, age) VALUES($1, $2)
    ''', name, age)
    print(f'Inserted user: {name}, {age}')

async def update_user_age(conn, user_id, new_age):
    await conn.execute('''
        UPDATE users SET age = $1 WHERE id = $2
    ''', new_age, user_id)
    print(f'Updated user id {user_id} to age {new_age}')

async def query_users(conn):
    rows = await conn.fetch('''
        SELECT id, name, age FROM users
    ''')
    for row in rows:
        print(f'User {row["id"]}: {row["name"]}, {row["age"]} years old')

async def main():
    conn = await asyncpg.connect(user='your_user', password='your_password',
                                 database='testdb', host='127.0.0.1')

    # Insert a new user
    await insert_user(conn, 'Alice', 30)
    
    # Insert another user
    await insert_user(conn, 'Bob', 25)

    # Update user's age
    await update_user_age(conn, 1, 35)

    # Query all users
    await query_users(conn)

    await conn.close()

# Run the main function
asyncio.run(main())
