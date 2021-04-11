with open("text.txt","r") as file:
    data = file.readlines()
with open("text1.txt", "w") as file:
    for i in range(len(data)):
        punct_count = data[i].count(".") + data[i].count("?") + data[i].count("!") + data[i].count("-") + data[i].count(",") + data[i].count("'")
        letter_count = len([k for k in data[i] if k.isalpha()])
        file.write(f"Line {i+1}: {data[i][:-1]}. ({letter_count})({punct_count})\n")
