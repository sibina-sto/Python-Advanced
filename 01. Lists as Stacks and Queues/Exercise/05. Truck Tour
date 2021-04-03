from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    petrol, distance = list(map(int, input().split()))
    pumps.append([petrol, distance])


original_pumps = pumps.copy()
additional_petrol = 0
index = 0


while index < len(pumps):
    curr_pump = pumps[index]
    petrol = pumps[index][0]
    distance = pumps[index][1]

    if petrol + additional_petrol >= distance:
        additional_petrol += petrol - distance
        index += 1
    else:
        pumps.append(pumps.popleft())
        additional_petrol = 0
        index = 0

print(original_pumps.index(pumps[0]))
