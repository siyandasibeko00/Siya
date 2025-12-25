menu = ["Eggs", "Milk", "Rice", "Toothpaste"]
stock = {menu[0]: 60, menu[1]: 80, menu[2]: 85, menu[3]: 120}
price = {menu[0]: 90, menu[1]: 100, menu[2]: 75, menu[3]: 65}

print(menu)
print(stock)
print(price)

total_stock = {}
for key in stock:
    if key in price:
        total_stock[key] = stock[key] * price[key]

print(total_stock)
