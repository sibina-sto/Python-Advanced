def get_odd_and_even_sets(n):
    odd_nums = set()
    even_nums = set()

    for line in range(1, n + 1):
        name = input()

        name_ascii_sum = sum([ord(char) for char in name])
        devised_num = name_ascii_sum // line

        if devised_num % 2 == 0:
            even_nums.add(devised_num)
        else:
            odd_nums.add(devised_num)

    return odd_nums, even_nums


def print_result(odd_nums_sum, even_nums_sum, odd_nums, even_nums):
    if odd_nums_sum == even_nums_sum:
        union_values = odd_nums.union(even_nums)
        print(', '.join(map(str, union_values)))
    elif odd_nums_sum > even_nums_sum:
        different_values = odd_nums.difference(even_nums)
        print(', '.join(map(str, different_values)))
    else:
        symmetric_different_values = even_nums.symmetric_difference(odd_nums)
        print(', '.join(map(str, symmetric_different_values)))


odd_nums, even_nums = get_odd_and_even_sets(int(input()))
odd_nums_sum = sum(odd_nums)
even_nums_sum = sum(even_nums)
print_result(odd_nums_sum, even_nums_sum, odd_nums, even_nums)
