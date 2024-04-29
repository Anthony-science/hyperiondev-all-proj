menu = ["Coffee", "Muffin", "Croissant", "Milkshake"]
stock = {"Coffee": 100, "Muffin": 30, "Croissant": 15, "Milkshake": 20}
price = {"Coffee": 3, "Muffin": 4, "Croissant": 2, "Milkshake": 5}

item_values = {items: stock[items] * price[items] for items in price}
total_stock_value = sum(item_values.values())

print(f"Individual stock values are \n\n {item_values}")
print(f"\nTotal stock value is {total_stock_value}\n")