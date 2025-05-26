number_items = int(input("Number of items: "))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items: "))
total_price = 0
for i in range(number_items):
    item_price = float(input(f"Price of item {i + 1}: "))
    total_price += item_price
if total_price > 100:
    total_price = total_price * 0.9
print(f"Total price for {number_items} items is ${total_price:.2f}")