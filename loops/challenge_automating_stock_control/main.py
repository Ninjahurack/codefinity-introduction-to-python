# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}


discount_threshold = 100

#processing started
print("Processing Started!")

for search in inventory:   
    real = inventory.get(search)
    print(f"Processing {search}")
    current_stock = real[0]
    minimum_required_stock = real[1]
    restock_quantity = real[2]
    sale_status = real[3]
    while current_stock < minimum_required_stock:
        current_stock += restock_quantity
    inventory.update({search: [current_stock, minimum_required_stock, restock_quantity, False]})


print("Processing Complete!")
    