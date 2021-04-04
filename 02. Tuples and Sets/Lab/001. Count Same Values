def count_numbers(numbers):
    occurrences = {}

    for num in numbers:
        if num not in occurrences:
            occurrences[num] = 0
        occurrences[num] += 1

    return occurrences


def print_result(occurrences):
    for num, count in occurrences.items():
        print(f"{num} - {count} times")


numbers = list(map(float, input().split()))
print_result(count_numbers(numbers))
