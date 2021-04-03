from collections import deque

cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))
wasted_water = 0


while cups and bottles:
    curr_cup = cups[0]
    curr_bottle = bottles.pop()

    if curr_cup > curr_bottle:
        while curr_cup > 0:
            if curr_bottle < curr_cup:
                curr_cup -= curr_bottle
                curr_bottle = bottles.pop()
            else:
                curr_bottle -= curr_cup
                curr_cup = 0

    wasted_water += curr_bottle - curr_cup
    curr_cup = cups.popleft()


if bottles and not cups:
    print(f"Bottles: {' '.join(map(str, reversed(bottles)))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")
print(f"Wasted litters of water: {wasted_water}")
