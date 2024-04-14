menu = ["Coffee", "Muffin", "Croissant", "Milkshake"]
stock = {"Coffee": 100, "Muffin": 30, "Croissant": 15, "Milkshake": 20}
price = {"Coffee": 3, "Muffin": 4, "Croissant": 2, "Milkshake": 5}
# stock_keys = stock.keys()
# stock_num = stock.value()
# stock_price = price.value()
item_values = {k: stock[k] * price[k] for k in price}
total_stock_value = sum(item_values.values())

print(f"Individual stock values are \n\n {item_values}")
print(f"\nTotal stock value is {total_stock_value}\n")


