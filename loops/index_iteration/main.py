prices = [29.99, 45.50, 12.75, 38.20]
discount = [0.1, 0.2, 0.15, 0.05]
real = 0

for price in range(len(prices)):
    prices[price] -= prices[price] * discount[real]
    print(f"Updated price for item {price + 1}: ${prices[price]:.2f}")
    real = real + 1

    