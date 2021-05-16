from collections import deque
from math import floor
 
expression = deque(input().split())
saved_numbers = []
 
while True:
    current_element = expression.popleft()
 
    if current_element in "-+/*":
        result = int(saved_numbers[0])
 
        for number in saved_numbers[1:]:
            if current_element == "-":
                result -= int(number)
            elif current_element == "+":
                result += int(number)
            elif current_element == "/":
                result /= int(number)
            elif current_element == "*":
                result *= int(number)
 
        expression.appendleft(str(floor(result)))
        saved_numbers = []
 
        if len(expression) == 1:
            break
 
    else:
        saved_numbers.append(current_element)
 
print(expression[0])
