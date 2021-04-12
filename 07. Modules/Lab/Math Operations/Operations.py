def perform_sum(first_num, second_num):
    return first_num + second_num


def perform_subtraction(first_num, second_num):
    return first_num - second_num


def perform_multiplication(first_num, second_num):
    return first_num * second_num


def perform_division(first_num, second_num):
    return first_num / second_num


def perform_power_operation(first_num, second_num):
    return first_num ** second_num


def calculate(first_num, second_num, operator):
    if operator == "+":
        return perform_sum(first_num, second_num)
    if operator == "-":
        return perform_subtraction(first_num, second_num)
    if operator == "*":
        return perform_multiplication(first_num, second_num)
    if operator == "/":
        return perform_division(first_num, second_num)
    if operator == "^":
        return perform_power_operation(first_num, second_num)
