from collections import deque


def solve(kids, toss):
    kids = deque(kids)

    while len(kids) > 1:
        count = 1
        while count < toss:
            curr_kid = kids.popleft()
            kids.append(curr_kid)
            count += 1

        print(f"Removed {kids.popleft()}")

    print(f"Last is {kids.pop()}")


kids = input().split()
toss = int(input())
solve(kids, toss)
