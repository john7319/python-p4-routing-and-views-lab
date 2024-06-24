#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route("/print/<string:print_data>")
def print_string(print_data):
    print(print_data)
    return f'{print_data}'

@app.route("/count/<int:num_data>")
def count(num_data):
    count_string = '\n'.join(str(i) for i in range(num_data)) + '\n'
    return count_string


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 % num2
    else:
        return "Error: Unsupported operation"

    return str(result)