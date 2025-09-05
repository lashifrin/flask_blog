FUNCTION:
def create_simple(app, blueprint):
    """
    Create a simple calculator function

    :param app: Flask application object
    :type app: flask.Flask
    :param blueprint: Flask blueprint object
    :type blueprint: flask.Blueprint
    :return: A simple calculator function
    :rtype: Callable[[int, int], int]
    """
    @app.route("/simple", methods=["POST"])
    def simple_calculator():
        try:
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            result = num1 + num2
            return f"{num1} + {num2} = {result}"
        except ValueError as e:
            return "Invalid input", 400
    return simple_calculator

TESTS:
import unittest
from flask import Flask, Blueprint
from unittest.mock import patch

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint("test_simple", __name__)
        self.calculator = create_simple(self.app, self.blueprint)

    def test_valid_inputs(self):
        with patch("request.form") as mock_form:
            mock_form["num1"] = "5"
            mock_form["num2"] = "3"
            result = self.calculator()
            self.assertEqual(result, 8)

    def test_invalid_inputs(self):
        with patch("request.form") as mock_form:
            mock_form["num1"] = "a"
            mock_form["num2"] = "b"
            result = self.calculator()
            self.assertEqual(result, 0)

    def test_missing_inputs(self):
        with patch("request.form") as mock_form:
            del mock_form["num1"]
            result = self.calculator()
            self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()