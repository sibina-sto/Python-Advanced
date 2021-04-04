heroes = {hero: {"inventory": [], "cost": 0} for hero in input().split(", ")}

line = input()
while not line == "End":
    hero, item, cost = line.split("-")

    if item not in heroes[hero]["inventory"]:
        heroes[hero]["inventory"] += [item]
        heroes[hero]["cost"] += int(cost)

    line = input()

[print(f"{hero} -> Items: {len(data['inventory'])}, Cost: {data['cost']}") for hero, data in heroes.items()]
