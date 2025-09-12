FILENAME: email_validator

FUNCTION:
def validate_email(email: str) -> bool:
    """
    Check if an email is valid.

    :param email: Email address to check
    :return: True if the email is valid, False otherwise
    """
    import re

    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    return bool(re.match(regex, email))

TESTS:
from email_validator import validate_email

class TestEmailValidator(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(validate_email("test@example.com"))
    
    def test_invalid_email(self):
        self.assertFalse(validate_email("test.example.com"))
    
    def test_empty_string(self):
        self.assertFalse(validate_email(""))
    
    def test_non_string(self):
        with self.assertRaises(TypeError):
            validate_email(123)

if __name__ == "__main__":
    unittest.main()