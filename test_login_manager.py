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
```