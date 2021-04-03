from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
intelligence_value = int(input())
bullets_used = 0


while bullets and locks:
    curr_bullet = bullets.pop()
    curr_lock = locks[0]

    if curr_bullet <= curr_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    bullets_used += 1
    if bullets_used % gun_barrel_size == 0 and bullets:
        print("Reloading!")


if locks and not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - (bullets_used * bullet_price)}")
