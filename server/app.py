#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count (parameter):
    count_output = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return count_output


@app.route('/math/<int:param1>/<operator>/<int:param2>')
def math(param1, operator, param2):
    # Perform the calculation based on the operator
    if operator == '+':
        result = param1 + param2
    elif operator == '-':
        result = param1 - param2
    elif operator == '*':
        result = param1 * param2
    elif operator == '/' or operator == 'div':
        if param2 == 0:
            return "Error: Division by zero", 400  # Handle division by zero
        result = param1 / param2
    elif operator == '%' or operator == 'mod':
        result = param1 % param2
    else:
        return "Error: Unsupported operator", 400  # Handle unsupported operators

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
