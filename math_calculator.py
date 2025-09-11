def calculate(num1: float, num2: float, operation: str) -> float:
    """
    This function takes in two numbers and an operation and performs the calculation.
    :param num1: The first number to be calculated
    :type num1: float
    :param num2: The second number to be calculated
    :type num2: float
    :param operation: The operation to perform (e.g. +, -, *, /)
    :type operation: str
    :return: The result of the calculation
    :rtype: float
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid operation")