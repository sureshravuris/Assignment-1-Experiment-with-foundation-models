# Improving SQL Queries
import sqlite3

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    
    # Old Version: Raw SQL query with potential SQL injection risk
    """
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    """

    # New Version: Parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    user = cursor.fetchone()
    conn.close()
    return user

def update_user_email(user_id, new_email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Old Version: Raw SQL query with potential SQL injection risk
    """
    query = f"UPDATE users SET email = '{new_email}' WHERE id = {user_id}"
    cursor.execute(query)
    """

    # New Version: Parameterized query to prevent SQL injection
    query = "UPDATE users SET email = ? WHERE id = ?"
    cursor.execute(query, (new_email, user_id))

    conn.commit()
    conn.close()

# Improving SQL Queries
def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Old Version: Raw SQL query with potential SQL injection risk
    """
    query = f"DELETE FROM users WHERE id = {user_id}"
    cursor.execute(query)
    """

    # New Version: Parameterized query to prevent SQL injection
    query = "DELETE FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    conn.commit()
    conn.close()

# Example usage
user = get_user("john_doe")
if user:
    print(f"User found: {user}")
else:
    print("User not found")

update_user_email(1, "newemail@example.com")
delete_user(2)