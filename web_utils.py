def calculator(num1, num2, operation):
    """
    A simple calculator function that takes in two numbers and an operation, and returns the result of the calculation.
    
    :param num1: The first number for the calculation
    :type num1: int or float
    :param num2: The second number for the calculation
    :type num2: int or float
    :param operation: The operation to perform on the two numbers
    :type operation: str (one of '+', '-', '*', '/')
    
    :return: The result of the calculation
    :rtype: int or float
    """
    if not isinstance(num1, (int, float)):
        raise TypeError("num1 must be an integer or a float")
    if not isinstance(num2, (int, float)):
        raise TypeError("num2 must be an integer or a float")
    if operation not in ['+', '-', '*', '/']:
        raise ValueError("operation must be one of '+', '-', '*', '/'")
    
    result = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else float('inf'),
    }[operation]