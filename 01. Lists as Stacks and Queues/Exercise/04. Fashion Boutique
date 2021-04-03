clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_count = 1

curr_sum = 0
while clothes:
    if curr_sum + clothes[-1] <= rack_capacity:
        curr_sum += clothes.pop()
    else:
        racks_count += 1
        curr_sum = 0

print(racks_count)
