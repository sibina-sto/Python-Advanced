from tribonacci_sequence import create_sequence, locate

curr_sequence = []

line = input()
while not line == "Stop":
    tokens = line.split()
    command = tokens[0]

    if command == "Create":
        count = int(tokens[2])
        curr_sequence = create_sequence(count)
        print(' '.join(map(str, curr_sequence)))

    elif command == "Locate":
        number = int(tokens[1])
        locate(number, curr_sequence)

    line = input()
