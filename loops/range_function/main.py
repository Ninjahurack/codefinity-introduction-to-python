# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for indices in range(5):
    week = weekdays[indices]
    promotion = daily_promotions[indices]
    print(f"{week}: Promotion on {promotion}")