box = []
for clothing in input().split():
    box.append(int(clothing))
rack_capacity = int(input())

total_racks = 1
current_rack = 0

for i in range(len(box)):
    current_clothing = box.pop()
    if current_clothing + current_rack > rack_capacity:
        total_racks += 1
        current_rack = 0
    current_rack += current_clothing

print(total_racks)
