# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
Run = 100
Walk = 30

for items in inventory:
    current_stock = inventory.get(items)
    discounted_price = inventory.get(items)
    regular_price = inventory.get(items)
    if current_stock[0] < 30:
        print(f"{items} need restocking.")
    if current_stock[0] > 100:
        print(f"{items} should be sold at the discounted price of {discounted_price[2]}.")
    if Walk < current_stock[0] < Run:
        print(f"{items} should be sold at the regular price of {regular_price[1]}.")

        