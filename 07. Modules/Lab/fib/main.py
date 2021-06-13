from modules.fibonacci.helper import generate_sequence, find_number


command = input()

while not command == "Stop":
    data = command.split()
    if data[0] == "Create":
        fibonacci_nums = generate_sequence(int(data[-1]))
        print(fibonacci_nums)
    else:
        result = find_number(int(data[-1]), fib_nums)
        print(f"The number - {int(data[-1])} is "
              f"at index {result}" if isinstance(result, int)
              else result)
    command = input()
