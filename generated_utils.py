FILENAME: login_handler.py

FUNCTION:
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

TESTS:
import login_handler
from flask import Flask, Request
from flask.sessions import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def test_add_login():
    # Create a mock request and user object
    request = Request({"username": "test_user", "password": "test_pass"})
    user = {"username": "test_user", "password": "test_pass"}
    
    # Create a mock database session
    engine = create_engine("sqlite://")
    Session.configure(bind=engine)
    db_session = Session()
    
    # Add the user to the database
    login_handler.add_login(request, user["username"], user["password"])
    
    # Check if the user was added successfully
    assert db_session.query(User).filter_by(username=user["username"]).first() is not None

def test_add_login_existing_user():
    # Create a mock request and user object
    request = Request({"username": "test_user", "password": "test_pass"})
    user = {"username": "test_user", "password": "test_pass"}
    
    # Create a mock database session
    engine = create_engine("sqlite://")
    Session.configure(bind=engine)
    db_session = Session()
    
    # Add the user to the database
    login_handler.add_login(request, user["username"], user["password"])
    
    # Check if the user was added successfully
    assert db_session.query(User).filter_by(username=user["username"]).first() is not None

def test_add_login_invalid_password():
    # Create a mock request and user object
    request = Request({"username": "test_user", "password": "test_pass12345"})
    user = {"username": "test_user", "password": "test_pass"}
    
    # Create a mock database session
    engine = create_engine("sqlite://")
    Session.configure(bind=engine)
    db_session = Session()
    
    # Add the user to the database
    login_handler.add_login(request, user["username"], "test_pass12345")
    
    # Check if the user was added successfully
    assert db_session.query(User).filter_by(username=user["username"]).first() is None