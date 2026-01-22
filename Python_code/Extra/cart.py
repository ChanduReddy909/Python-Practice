Available = {
    "Tomato": 40,
    "Onion": 40,
    "Chilli": 70,
    "Potato": 35,
    "Carrot": 60,
    "Betroat": 70,
    "Brinjal": 60,
    "Radis": 60,
    "Mashroom": 130,
    "Garlic": 170
}

cart = {}

items_list = list(Available.items())

print("Welcome to shopping cart")
print("Available items\n")

for i in range(len(items_list)):
    item_name, price = items_list[i]
    print(f"{i+1}. {item_name} --> Rs.{price}")

print("\nNote: All items are available in KGs only")

print("\n1. Add")
print("2. Show Cart")
print("3. Remove")
print("4. Order")
print("5. Exit")

while True:
    choice = int(input("\nEnter choice: "))

    # ---------- CHOICE 1 : ADD ITEMS ----------
    if choice == 1:
        print("\n--- Add Items ---")

        for i in range(len(items_list)):
            item_name, price = items_list[i]
            print(f"{i+1}. {item_name} - Rs.{price}")

        while True:
            user_input = input("\nSelect item number (or type 'exit'): ")

            if user_input.lower() == "exit":
                break

            item_no = int(user_input) - 1

            if item_no < 0 or item_no >= len(items_list):
                print("Invalid item number. Try again.")
                continue

            selected_item, price = items_list[item_no]
            quantity = int(input(f"Enter quantity (KG) for {selected_item}: "))

            if selected_item in cart:
                cart[selected_item] += quantity
            else:
                cart[selected_item] = quantity

            print(f"{selected_item} ({quantity} KG) added to cart.")

    # ---------- CHOICE 2 : SHOW CART ----------
    elif choice == 2:
        if not cart:
            print("\nCart is empty")
        else:
            print("\nYour Cart")
            print(f"{'Item Name':<10} | {'Quantity':<8} | {'Price':<5} | {'Total':<5}")
            print("-" * 40)

            for name, quantity in cart.items():
                price = Available[name]
                total = price * quantity
                print(f"{name:<10} | {quantity:<8} | {price:<5} | {total:<5}")

    # ---------- CHOICE 3 : REMOVE ITEM ----------
    elif choice == 3:
        if not cart:
            print("\nCart is empty")
        else:
            cart_items = list(cart.keys())

            print("\n--- Remove Item ---")
            for i in range(len(cart_items)):
                print(f"{i+1}. {cart_items[i]}")

            while True:
                user_input = input("\nSelect item number to remove (or type 'exit'): ")

                if user_input.lower() == "exit":
                    break

                item_no = int(user_input) - 1

                if item_no < 0 or item_no >= len(cart_items):
                    print("Invalid number. Try again.")
                    continue

                removed_item = cart_items[item_no]
                del cart[removed_item]

                print(f"{removed_item} removed from cart.")
                break

    # ---------- CHOICE 4 : ORDER / BILL ----------
    elif choice == 4:
        if not cart:
            print("\nCart is empty. Cannot place order.")
        else:
            print("\n------ FINAL BILL ------")
            print(f"{'Item Name':<10} | {'Quantity':<8} | {'Price':<5} | {'Total':<5}")
            print("-" * 40)

            grand_total = 0

            for name, quantity in cart.items():
                price = Available[name]
                total = price * quantity
                grand_total += total
                print(f"{name:<10} | {quantity:<8} | {price:<5} | {total:<5}")

            print("-" * 40)
            print(f"{'Grand Total':<26} Rs.{grand_total}")
            print("\nThank you for your order!")
            break

    # ---------- EXIT ----------
    elif choice == 5:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Try again.")
