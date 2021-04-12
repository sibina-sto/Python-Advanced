def create_sequence(n):
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 2] + sequence[i - 1])
    return sequence


def locate(number, curr_sequence):
    if number in curr_sequence:
        print(f"The number - {number} is at index {curr_sequence.index(number)}")
    else:
        print(f"The number {number} is not in the sequence")
