from math_operations import calculate

first_num, operator, second_num = input().split()

result = calculate(float(first_num), int(second_num), operator)
print(f"{result:.2f}")
