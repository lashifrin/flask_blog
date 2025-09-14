import unittest
from login_manager import add_login

class TestAddLogin(unittest.TestCase):
    def test_add_login_valid(self):
        """
        Test adding a new user to the database with valid input.
        """
        # Set up the test data
        username = "johndoe"
        password = "123456"
        
        # Call the function and check the result
        result = add_login(username, password)
        self.assertTrue(result)
    
    def test_add_login_invalid(self):
        """
        Test adding a new user to the database with invalid input.
        """
        # Set up the test data
        username = "johndoe"
        password = None
        
        # Call the function and check the result
        result = add_login(username, password)
        self.assertFalse(result)
    
    def test_add_login_duplicate(self):
        """
        Test adding a new user to the database with a duplicate username.
        """
        # Set up the test data
        username = "johndoe"
        password = "123456"
        
        # Call the function and check the result
        result = add_login(username, password)
        self.assertFalse(result)
    
    def test_add_login_empty(self):
        """
        Test adding a new user to the database with empty input.
        """
        # Set up the test data
        username = ""
        password = "123456"
        
        # Call the function and check the result
        result = add_login(username, password)
        self.assertFalse(result)
    
    def test_add_login_invalid_type(self):
        """
        Test adding a new user to the database with invalid input type.
        """
        # Set up the test data
        username = "johndoe"
        password = 123456
        
        # Call the function and check the result
        result = add_login(username, password)
        self.assertFalse(result)
```