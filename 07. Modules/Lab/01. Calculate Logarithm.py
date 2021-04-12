from math import log


def calculate_log(number, base):
    if base == "natural":
        return log(number)
    else:
        base = int(base)
        return log(number, base)


number = int(input())
base = input()

print(f"{calculate_log(number, base):.2f}")
