from collections import deque

parentheses_sequence = list(input())

if len(parentheses_sequence) % 2 == 1:
    print("NO")
    exit()


valid_pairs = [("(", ")"), ("[", "]"), ("{", "}")]
opening_parentheses = deque([symbol for symbol in parentheses_sequence if symbol in ("(", "[", "{")])
closing_parentheses = deque([symbol for symbol in parentheses_sequence if symbol in (")", "]", "}")])

if not opening_parentheses or not closing_parentheses:
    print("NO")
    exit()


while opening_parentheses and closing_parentheses:
    if (opening_parentheses[-1], closing_parentheses[-1]) in valid_pairs:
        opening_parentheses.pop()
        closing_parentheses.pop()
    elif (opening_parentheses[0], closing_parentheses[0]) in valid_pairs:
        opening_parentheses.popleft()
        closing_parentheses.popleft()
    elif (opening_parentheses[-1], closing_parentheses[0]) in valid_pairs:
        opening_parentheses.pop()
        closing_parentheses.popleft()
    else:
        print("NO")
        break
else:
    print("YES")
