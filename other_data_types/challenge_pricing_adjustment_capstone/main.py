grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

eggs = grocery_inventory.get("Eggs")
price_1 = eggs[1]
print(price_1)
if price_1 > 5.00:
   print("Eggs are too expensive, reducing the price by $1.")
   grocery_inventory.update({"Eggs": ("Dairy", 4.50, 30)})
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

Milks = grocery_inventory.get("Milk")
Milk1 = Milks[2]
if Milk1 < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk": ("Dairy", 3.50, 28)})
else: 
    print("Milk has sufficient stock.")

expensive = grocery_inventory.get("Apples")
expensive1 = expensive[1]

if expensive1 > 2:
    grocery_inventory.remove("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)