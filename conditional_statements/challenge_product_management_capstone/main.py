# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"
Perishable_indeed = False

if product_type == "Perishable":
    Perishable_indeed = True    

if days_until_expiration <= 3 and stock_level > 50:
    print("30% discount applied")
elif 4 <= days_until_expiration <= 6 and stock_level > 50:      
    print("20% discount applied")
elif days_until_expiration > 6 and stock_level <= 50:
    print("10% discount applied")

if Perishable_indeed == False:
    print("No discount available for non-perishable items.")