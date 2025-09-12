def calculate(num1, num2, operation):
    """
    Calculate the result of two numbers based on a given operation.

    :param num1: The first number (float or int)
    :param num2: The second number (float or int)
    :param operation: The operation to perform (str)
    :return: The result of the calculation (float or int)
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Invalid input: num1 and num2 must be numerical values.")
    if not isinstance(operation, str):
        raise ValueError("Invalid input: operation must be a string.")
    if operation.lower() == "add":
        result = num1 + num2
    elif operation.lower() == "subtract":
        result = num1 - num2
    elif operation.lower() == "multiply":
        result = num1 * num2
    elif operation.lower() == "divide":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError(f"Invalid operation: {operation}")
    return result