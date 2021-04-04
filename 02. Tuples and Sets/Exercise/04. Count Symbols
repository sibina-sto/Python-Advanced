def count_symbol_occurrences(text):
    occurrences = {}

    for symbol in text:
        if symbol not in occurrences:
            occurrences[symbol] = 0
        occurrences[symbol] += 1

    return occurrences


def print_result(occurrences):
    for symbol, count in sorted(occurrences.items()):
        print(f"{symbol}: {count} time/s")


symbol_occurrences = count_symbol_occurrences(input())
print_result(symbol_occurrences)
