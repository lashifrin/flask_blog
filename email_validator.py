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