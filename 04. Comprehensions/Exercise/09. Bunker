categories = {category: {} for category in input().split(", ")}
n = int(input())

for _ in range(n):
    category, item, data = input().split(" - ")
    quantity_data, quality_data = data.split(";")
    quality = int(quality_data.split(":")[1])
    quantity = int(quantity_data.split(":")[1])

    categories[category][item] = (quality, quantity)

total_quantity = sum([quantity
                      for category, items in categories.items()
                      for item, (quality, quantity) in items.items()])

total_quality = sum([quality
                     for category, items in categories.items()
                     for item, (quality, quantity) in items.items()])

print(f"Count of items: {total_quantity}\n"
      f"Average quality: {total_quality / len(categories):.2f}")

[print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]
