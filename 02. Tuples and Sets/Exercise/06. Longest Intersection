def find_range_values(curr_range):
    return list(map(int, curr_range.split(",")))


def find_set(curr_range):
    start_value, end_value = find_range_values(curr_range)
    curr_set = set(range(start_value, end_value + 1))

    return curr_set


def find_longest_intersection(n):
    longest_intersection = set()

    for _ in range(n):
        first_range, second_range = input().split("-")
        first_set = find_set(first_range)
        second_set = find_set(second_range)

        curr_intersection = first_set.intersection(second_set)

        if len(curr_intersection) > len(longest_intersection):
            longest_intersection = curr_intersection

    return list(longest_intersection)


def print_result(longest_intersection):
    print(f"Longest intersection is {longest_intersection} "
          f"with length {len(longest_intersection)}")


print_result(find_longest_intersection(int(input())))
