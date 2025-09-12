FILENAME: login_manager.py

FUNCTION:
def add_login(username: str, password: str) -> None:
    """
    Adds a new user to the login database with the given username and password.

    :param username: The username of the new user.
    :type username: str
    :param password: The password of the new user.
    :type password: str
    :return: None.
    """
    # Implement login database connection and insertion here

TESTS:
import unittest
from login_manager import add_login

class TestLoginManager(unittest.TestCase):
    def test_add_login(self):
        username = "testuser"
        password = "testpassword"
        add_login(username, password)
        # Implement login database query and assertion here

if __name__ == '__main__':
    unittest.main()