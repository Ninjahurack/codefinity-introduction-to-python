#defining initial lists
produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
#combined lists
groceries = [produce] + [dairy]
#for loop to iterate through groceries 
for section in groceries:
    print(section)
    for item in section:
        print(item)