import os
command = input()
while command != "End":
    command = command.split("-")
    file_name = command[1]
    if command[0] == "Create":
        with open(f"{file_name}","w") as file:
            file.write("")

    elif command[0] == "Add":
        content = command[2]
        try:
            with open(f"{file_name}","a") as file:
                file.write(f"{content}\n")
        except FileNotFoundError:
            with open(f"{file_name}","w") as file:
                file.write(f"{content}")

    elif command[0] == "Replace":
        try:
            with open(f"{file_name}","r") as file:
                old_string, new_string = command[2], command[3]
                text = file.read()
            new = text.replace(old_string,new_string)
            with open(f"{file_name}","w") as file:
                file.write(new)
        except FileNotFoundError:
            print("An error occured")
    elif command[0] == "Delete":
        try:
            os.remove(f"{file_name}")
        except FileNotFoundError:
            print("An error occured")
    command = input()
