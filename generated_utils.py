FILENAME: login_manager

FUNCTION:
def add_login(username, password):
    """Add login functionality for web operations.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        bool: True if the login is successful, False otherwise.
    """
    # Your code here
    return True

TESTS:
from login_manager import add_login

class TestAddLogin(unittest.TestCase):
    def test_add_login_successful(self):
        result = add_login("test_user", "test_password")
        self.assertTrue(result)

    def test_add_login_failed(self):
        result = add_login("test_user", "wrong_password")
        self.assertFalse(result)