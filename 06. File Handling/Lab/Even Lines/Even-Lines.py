import re
def replacings(data):
    regex = r"[\-\.\,\!\?]"
    return re.sub(regex, "@", data)

with open("text.txt", "r") as file:
    data = file.readlines()
    for i in range(len(data)):
        if i % 2 == 0:
            result = replacings(data[i]).split()
            result = ' '.join(result[::-1])
            print(result)
