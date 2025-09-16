import unittest
from email_validator import add_email

class TestEmailValidator(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(add_email("john.doe@example.com"))
    
    def test_invalid_email(self):
        self.assertFalse(add_email("johndoeexample.com"))
    
    def test_valid_email_with_hyphen(self):
        self.assertTrue(add_email("john-doe@example.com"))
    
    def test_valid_email_with_underscore(self):
        self.assertTrue(add_email("john_doe@example.com"))
    
    def test_invalid_email_with_special_characters(self):
        self.assertFalse(add_email("johndoe!@#$%^&*()_+-={}[]|\:;'<>?,./\"example.com"))
    
    def test_valid_email_with_different_tld(self):
        self.assertTrue(add_email("john.doe@example.net"))
    
if __name__ == "__main__":
    unittest.main()
```