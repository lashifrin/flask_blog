def add_login(username, password):
    """
    Adds a new user to the login system.

    :param username: The username of the new user
    :type username: str
    :param password: The password of the new user
    :type password: str
    :return: A boolean indicating whether the user was added successfully
    :rtype: bool
    """
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings.")

    user_exists = check_user_exists(username)
    if user_exists:
        return False

    create_new_user(username, password)
    return True