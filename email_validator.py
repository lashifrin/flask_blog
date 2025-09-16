def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    :param email: The email address to validate.
    :type email: str
    :return: True if the email is valid, False otherwise.
    :rtype: bool
    """
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(regex, email) is not None