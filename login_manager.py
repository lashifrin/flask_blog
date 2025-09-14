def add_login(username, password):
    """
    Adds a new user to the login database.
    
    Parameters:
        username (str): The username of the new user.
        password (str): The password of the new user.
    
    Returns:
        bool: True if the addition was successful, False otherwise.
    """
    # Check if the username already exists
    if username in users:
        return False
    
    # Add the new user to the database
    users[username] = password
    return True