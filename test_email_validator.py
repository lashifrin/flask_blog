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
```