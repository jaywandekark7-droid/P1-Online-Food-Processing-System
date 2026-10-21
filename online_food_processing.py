from collections import deque

orders = deque()
completed_orders = []

while True:
    print("\n--- Online Food Processing System ---")
    print("1. Place Order")
    print("2. View Pending Orders")
    print("3. Process Next Order")
    print("4. View Completed Orders")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        customer = input("Enter customer name: ").strip()
        food = input("Enter food item: ").strip()

        if not customer or not food:
            print("Name and food item cannot be empty.")
        else:
            orders.append({"customer": customer, "food": food})
            print("Order placed successfully.")

    elif choice == "2":
        if not orders:
            print("No pending orders.")
        else:
            print("\nPending Orders:")
            for i, order in enumerate(orders, 1):
                print(i, order["customer"], "-", order["food"])

    elif choice == "3":
        if not orders:
            print("No orders to process.")
        else:
            order = orders.popleft()
            completed_orders.append(order)
            print("Processed:", order["customer"], "-", order["food"])

    elif choice == "4":
        if not completed_orders:
            print("No completed orders.")
        else:
            print("\nCompleted Orders:")
            for order in completed_orders:
                print(order["customer"], "-", order["food"])

    elif choice == "5":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Try again.")
