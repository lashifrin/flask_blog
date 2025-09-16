FILENAME: login_manager.py

FUNCTION:
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

TESTS:
import unittest
from login_manager import add_login

class TestAddLogin(unittest.TestCase):
    def test_add_login_valid(self):
        result = add_login("test_user", "test_pass")
        self.assertTrue(result)

    def test_add_login_invalid(self):
        with self.assertRaises(ValueError):
            add_login(123, "test_pass")

    def test_add_login_user_exists(self):
        create_new_user("existing_user", "existing_pass")
        result = add_login("existing_user", "test_pass")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()