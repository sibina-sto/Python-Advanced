from collections import deque


def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0

    return h, m, s


robot_info = input().split(";")
time = list(map(int, input().split(":")))
robots_dict = {}
available_robots = deque()
waiting_robots = deque()
products = deque()

product = input()
while not product == "End":
    products.append(product)
    product = input()


for robot in robot_info:
    name, processing_time = robot.split("-")
    processing_time = int(processing_time)
    available_robots.append([name, processing_time])
    robots_dict[name] = processing_time


while products:
    for robot in waiting_robots:
        name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            available_robots.append([name, robots_dict[name]])
    waiting_robots = [robot for robot in waiting_robots if robot[1] > 0]

    time = next_second(time[0], time[1], time[2])
    curr_product = products.popleft()

    if not available_robots:
        products.append(curr_product)
        continue

    curr_robot = available_robots.popleft()
    waiting_robots.append(curr_robot)
    print(f"{curr_robot[0]} - {curr_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
