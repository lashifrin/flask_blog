from login_manager import add_login

class TestAddLogin(unittest.TestCase):
    def test_add_login_successful(self):
        result = add_login("test_user", "test_password")
        self.assertTrue(result)

    def test_add_login_failed(self):
        result = add_login("test_user", "wrong_password")
        self.assertFalse(result)
```