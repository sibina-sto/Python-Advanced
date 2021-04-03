n = int(input())
numbers = []

for _ in range(n):
    tokens = input().split()
    query = tokens[0]

    if query == "1":
        num = int(tokens[1])
        numbers.append(num)

    elif query == "2" and numbers:
        numbers.pop()

    elif query == "3" and numbers:
        print(max(numbers))

    elif query == "4" and numbers:
        print(min(numbers))


print(', '.join(map(str, reversed(numbers))))
