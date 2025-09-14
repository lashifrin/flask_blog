def add_login(request, username, password):
    """
    Adds a new user to the login database.
    
    Parameters:
        request (flask.Request): The incoming Flask request object.
        username (str): The user's username.
        password (str): The user's password.
    
    Returns:
        bool: True if the user was added successfully, False otherwise.
    """
    # Check if the username is already taken
    if not request.session.query(User).filter_by(username=username).first():
        # Create a new User object
        user = User(username=username, password=password)
        # Add the user to the database
        db.session.add(user)
        db.session.commit()
        return True
    else:
        return False