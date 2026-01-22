from datetime import datetime

# ---------- USER DETAILS ----------
name = input("Enter your name: ")

# ---------- ITEM LIST ----------
lists = '''
=========== Available Items ===========
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
Paneer  Rs 110/kg
Maggi   Rs 50/pack
Boost   Rs 90/bottle
Colgate Rs 85/each
=======================================
'''

# ---------- PRICE DICTIONARY ----------
items = {
    'rice': 20,
    'sugar': 30,
    'salt': 20,
    'oil': 80,
    'paneer': 110,
    'maggi': 50,
    'boost': 90,
    'colgate': 85
}

# ---------- VARIABLES ----------
cart_items = []
cart_qty = []
cart_price = []

total_price = 0
gst = 0
final_amount = 0

# ---------- SHOW ITEM LIST ----------
option = int(input("For list of items press 1: "))
if option == 1:
    print(lists)

# ---------- SHOPPING LOOP ----------
while True:
    choice = int(input("\nEnter 1 to buy | 2 to generate bill: "))

    if choice == 2:
        break

    if choice == 1:
        item = input("Enter item name: ").lower()
        if item in items:
            quantity = int(input("Enter quantity: "))
            price = quantity * items[item]

            cart_items.append(item)
            cart_qty.append(quantity)
            cart_price.append(price)

            total_price += price
            print(f"Added {item} - Rs {price}")
        else:
            print("❌ Item not available")

    else:
        print("❌ Invalid choice")

# ---------- BILL GENERATION ----------
if total_price != 0:
    gst = (total_price * 5) / 100
    final_amount = total_price + gst

    print("\n")
    print(25 * "=", "Veggie Super Market", 25 * "=")
    print(30 * " ", "Wanaparthy")
    print(f"Name: {name:<20} Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print(75 * "-")
    print("S.No", "Item".ljust(15), "Qty".ljust(10), "Price")
    print(75 * "-")

    for i in range(len(cart_items)):
        print(i+1, "  ", cart_items[i].ljust(15), str(cart_qty[i]).ljust(10), cart_price[i])

    print(75 * "-")
    print("Total Amount".ljust(40), "Rs", total_price)
    print("GST (5%)".ljust(40), "Rs", gst)
    print(75 * "-")
    print("Final Amount".ljust(40), "Rs", final_amount)
    print(75 * "-")
    print(25 * " ", "Thanks for visiting 🙏")
    print(75 * "-")

else:
    print("No items purchased.")
