def get_subexpressions(expression):
    opening_brackets = []
    subexpressions = []

    for index, char in enumerate(expression):
        if char == "(":
            opening_brackets.append(index)
        elif char == ")":
            last_opening_bracket_index = opening_brackets.pop()
            subexpressions.append(expression[last_opening_bracket_index:index + 1])

    return "\n".join(subexpressions)


expression = input()
print(get_subexpressions(expression))
