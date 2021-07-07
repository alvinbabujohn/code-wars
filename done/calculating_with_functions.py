"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def do_ops(left, op, right):
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if op == "/":
        return left // right


def zero(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(0, op, right)
    return 0


def one(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(1, op, right)
    return 1


def two(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(2, op, right)
    return 2


def three(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(3, op, right)
    return 3


def four(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(4, op, right)
    return 4


def five(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(5, op, right)
    return 5


def six(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(6, op, right)
    return 6


def seven(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(7, op, right)
    return 7


def eight(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(8, op, right)
    return 8


def nine(op_right=None):
    if op_right:
        op, right = op_right
        return do_ops(9, op, right)
    return 9


def plus(right):
    return ("+", right)


def minus(right):
    return ("-", right)


def times(right):
    return ("*", right)


def divided_by(right):
    return ("/", right)


print("Basic Tests")
print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)
