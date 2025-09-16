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
```