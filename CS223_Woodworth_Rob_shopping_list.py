sub_total, total_price, tax = float(0), float(0), float(0.089)
items = ["Milk", "Eggs", "Cereal", "Beef", "Bacon", "Cake", "TP", "Gift Card"]
prices = [3.49, 1.99, 4.49, 3.99, 5.99, 29.99, 5.49, 74.99]
print(f"\n=== Bobbo\'s Grocery Store ===\n\n===========================\n")
for i, (name, price) in enumerate(zip(items, prices), start=1):
    print(f"{i}: {name} for ${price}")
cart, pR, sel = [], [], 0
while sel != 'x':
    sel = input("Item number to add to cart or enter x to checkout: ")
    if sel == "x": break
    elif sel.isnumeric() is False: print("ERROR: Enter 1 to 8 to add item")
    elif 1 <= int(sel) <= 8:
        cart.append(items[int(sel)-1]), pR.append(prices[int(sel)-1])
        print(f"{items[int(sel)-1]} was added. \nCart: {cart}\n")
    else:print("ERROR: Enter 1 to 8 to add item, or x to checkout")
print("\n=== Your receipt: ===\n")
for i, (name, price) in enumerate(zip(cart, pR), start=1):
    print(f"{i}: {name} for ${price}")
print(f"\nSubtotal: ${sum(pR):,.2f}\n8.9% tax: ${sum(pR) * tax:,.2f}")
print(f"Total Price: ${sum(pR)+(sum(pR)*tax):,.2f}\n\nThanks from Bobbo\'s!")
