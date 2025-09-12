def add_login(username, password):
    """
    Add a new login to the database.

    :param username: The username of the user
    :type username: str
    :param password: The password of the user
    :type password: str
    :return: True if the login was added successfully, False otherwise
    :rtype: bool
    """
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO logins (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Error adding login: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()