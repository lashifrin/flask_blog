FILENAME: email_validator
  
FUNCTION:
def add_email(address):
    """
    Adds an email address to a list of validated emails.
    
    Parameters:
        address (str): The email address to validate.
        
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Import required modules
    import re
    
    # Define regex pattern for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # Compile the pattern and match it against the input address
    email_regex = re.compile(pattern)
    if not email_regex.match(address):
        return False
    
    # If the email is valid, add it to the list of validated emails
    validated_emails.append(address)
    return True
  
TESTS:
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