cart = []

while True:
    action = input("Add/Remove/View/Exit: ").lower()

    if not action:
        print("Please enter a valid action.")
        continue

    if action == "add":
        item = input("Enter item to add: ")
        cart.append(item)
        print(f"{item} added to cart.")

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")

    elif action == "view":
        if cart:
            print("Your cart contains:")
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item}")
        else:
            print("Your cart is empty.")
            
    elif action == "exit":
        print(f"Final cart items: {cart}")
        break
    else:
        print("Invalid choice.")
