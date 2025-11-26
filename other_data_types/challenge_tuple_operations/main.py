# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#Apples
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

#Bananas
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")


#Apples
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
print(f"Number of Apples {apple_count}")
#Grapes
grape_count = shelf.count("grapes")

if grape_count == 1:
    print("Grapes need to be restocked.")
else: 
    print("Grapes are sufficiently stocked.")

#Oranges
oranges_count = shelf.count("oranges")
oranges_index = shelf.index("oranges")
if "oranges" in shelf:
    print(f"Oranges are at index: {oranges_index}")
else:
    print("Oranges are out of stock.")
    