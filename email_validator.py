def validate_email(email: str) -> bool:
    """
    Check if an email is valid.

    :param email: Email address to check
    :return: True if the email is valid, False otherwise
    """
    import re

    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    return bool(re.match(regex, email))