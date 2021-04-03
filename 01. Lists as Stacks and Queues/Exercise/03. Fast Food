from collections import deque

food_quantity = int(input())
order_quantities = deque(map(int, input().split()))

print(max(order_quantities))

while food_quantity > 0 and order_quantities:
    if order_quantities[0] > food_quantity:
        print(f"Orders left: {' '.join(map(str, order_quantities))}")
        break

    food_quantity -= order_quantities.popleft()
else:
    print("Orders complete")
