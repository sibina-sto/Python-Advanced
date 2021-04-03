from collections import deque


def add_people():
    people = deque()

    name = input()
    while not name == "Start":
        people.append(name)
        name = input()

    return people


def serve_people(people, quantity):
    while True:
        command = input().split()
        if command[0] == "End":
            print(f"{quantity} liters left")
            break
        elif command[0] == "refill":
            liters = int(command[1])
            quantity += liters
        else:
            liters = int(command[0])

            if liters <= quantity:
                print(f"{people.popleft()} got water")
                quantity -= liters
            else:
                print(f"{people.popleft()} must wait")


quantity = int(input())
people = add_people()
serve_people(people, quantity)
