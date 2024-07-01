# Hellocafe.py

# Create a list of menu items
menu = ["Coffee", "Tea", "Sandwich", "Cake", "Coca Cola","Diet Cola"]

# Create a dictionary for stock values
stock = {
    "Coffee": 100,
    "Tea": 80,
    "Sandwich": 50,
    "Cake": 30,
    "Coca Cola": 30,
    "Diet Cola": 25
}

# Create a dictionary for prices
price = {
    "Coffee": 2.75,
    "Tea": 2.50,
    "Sandwich": 3.00,
    "Cake": 4.00,
    "Coca Cola": 1.75,
    "Diet Cola": 1.75
}

# Calculate the total stock worth
total_stock_worth = 0
for item in menu:
    item_stock_value = stock[item] * price[item]
    total_stock_worth += item_stock_value

# Print the result
print("\nTotal stock worth in the cafe: £{:.2f}".format(total_stock_worth))
