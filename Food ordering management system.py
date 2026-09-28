
# ============================================================
# FOOD ORDERING MANAGEMENT SYSTEM
# ============================================================
# A beginner-friendly Python project using Lists
#
# Main features:
#   Owner Panel
#       - Dashboard
#       - Manage Restaurants
#       - Manage Food Items
#       - View Orders
#       - Manage Users
#       - Reports
#
#   User Panel
#       - Browse Restaurants
#       - View Menu
#       - Add to Cart
#       - Place Order
#       - Track Order
#       - Order History
#
# Python list methods demonstrated:
#   append()
#   pop()
#   remove()
#   indexing
#   for loop
# ============================================================


# -----------------------------
# SAMPLE DATA
# -----------------------------

restaurant_list = [
    "Food Plaza",
    "Tasty Bites",
    "Spice Hub"
]

food_list = [
    {
        "name": "Pizza",
        "restaurant": "Food Plaza",
        "price": 250
    },
    {
        "name": "Burger",
        "restaurant": "Food Plaza",
        "price": 150
    },
    {
        "name": "Pasta",
        "restaurant": "Tasty Bites",
        "price": 200
    },
    {
        "name": "Fries",
        "restaurant": "Tasty Bites",
        "price": 100
    },
    {
        "name": "Sandwich",
        "restaurant": "Spice Hub",
        "price": 120
    }
]

user_list = [
    "User1",
    "User2"
]

order_list = []

order_status = [
    "Placed",
    "Preparing",
    "On the way",
    "Delivered"
]

cart_list = []


# ============================================================
# COMMON FUNCTIONS
# ============================================================

def line():
    print("-" * 60)


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# RESTAURANT MANAGEMENT
# ============================================================

def manage_restaurants():
    while True:
        print("\n===== MANAGE RESTAURANTS =====")
        print("1. View Restaurants")
        print("2. Add Restaurant")
        print("3. Update Restaurant")
        print("4. Remove Restaurant")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_restaurants()

        elif choice == "2":
            name = input("Enter restaurant name: ")

            if name:
                restaurant_list.append(name)
                print("Restaurant added successfully!")
            else:
                print("Restaurant name cannot be empty.")

        elif choice == "3":
            view_restaurants()

            if len(restaurant_list) > 0:
                try:
                    index = int(input("Enter restaurant number: ")) - 1

                    if 0 <= index < len(restaurant_list):
                        new_name = input("Enter new restaurant name: ")
                        restaurant_list[index] = new_name
                        print("Restaurant updated successfully!")
                    else:
                        print("Invalid number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            view_restaurants()

            if len(restaurant_list) > 0:
                try:
                    index = int(input("Enter restaurant number: ")) - 1

                    if 0 <= index < len(restaurant_list):
                        removed = restaurant_list.pop(index)
                        print(f"{removed} removed successfully!")
                    else:
                        print("Invalid number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def view_restaurants():
    print("\n===== RESTAURANTS =====")

    if not restaurant_list:
        print("No restaurants available.")
        return

    for i, restaurant in enumerate(restaurant_list, start=1):
        print(f"{i}. {restaurant}")


# ============================================================
# FOOD / MENU MANAGEMENT
# ============================================================

def manage_food_items():
    while True:
        print("\n===== MANAGE FOOD ITEMS =====")
        print("1. View Food Items")
        print("2. Add Food Item")
        print("3. Update Food Item")
        print("4. Remove Food Item")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_food_items()

        elif choice == "2":
            add_food_item()

        elif choice == "3":
            update_food_item()

        elif choice == "4":
            remove_food_item()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def view_food_items():
    print("\n===== FOOD MENU =====")

    if not food_list:
        print("No food items available.")
        return

    for i, food in enumerate(food_list, start=1):
        print(
            f"{i}. {food['name']} | "
            f"{food['restaurant']} | "
            f"₹{food['price']}"
        )


def add_food_item():
    view_restaurants()

    restaurant = input("Enter restaurant name: ")
    name = input("Enter food item name: ")

    try:
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid price.")
        return

    if restaurant not in restaurant_list:
        print("Restaurant does not exist.")
        return

    food = {
        "name": name,
        "restaurant": restaurant,
        "price": price
    }

    # Python list append()
    food_list.append(food)

    print("Food item added successfully!")


def update_food_item():
    view_food_items()

    if not food_list:
        return

    try:
        index = int(input("Enter food item number: ")) - 1

        if 0 <= index < len(food_list):
            new_name = input("Enter new food name: ")

            try:
                new_price = float(input("Enter new price: "))
            except ValueError:
                print("Invalid price.")
                return

            # Python list indexing
            food_list[index]["name"] = new_name
            food_list[index]["price"] = new_price

            print("Food item updated successfully!")

        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")


def remove_food_item():
    view_food_items()

    if not food_list:
        return

    try:
        index = int(input("Enter food item number: ")) - 1

        if 0 <= index < len(food_list):

            # Python list pop()
            removed = food_list.pop(index)

            print(f"{removed['name']} removed successfully!")

        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")


# ============================================================
# USER MANAGEMENT
# ============================================================

def manage_users():
    while True:
        print("\n===== MANAGE USERS =====")
        print("1. View Users")
        print("2. Add User")
        print("3. Remove User")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_users()

        elif choice == "2":
            username = input("Enter username: ")

            if username:
                user_list.append(username)
                print("User added successfully!")

        elif choice == "3":
            view_users()

            if user_list:
                try:
                    index = int(input("Enter user number: ")) - 1

                    if 0 <= index < len(user_list):
                        removed = user_list.pop(index)
                        print(f"{removed} removed successfully!")
                    else:
                        print("Invalid number.")

                except ValueError:
                    print("Invalid input.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def view_users():
    print("\n===== USERS =====")

    if not user_list:
        print("No users available.")
        return

    for i, user in enumerate(user_list, start=1):
        print(f"{i}. {user}")


# ============================================================
# ORDER MANAGEMENT
# ============================================================

def view_orders():
    print("\n===== ALL ORDERS =====")

    if not order_list:
        print("No orders available.")
        return

    for order in order_list:
        print(f"\nOrder ID: {order['id']}")
        print(f"User: {order['user']}")
        print(f"Restaurant: {order['restaurant']}")
        print(f"Items: {order['items']}")
        print(f"Total: ₹{order['total']}")
        print(f"Status: {order['status']}")


def track_order():
    if not order_list:
        print("No orders available.")
        return

    order_id = input("Enter Order ID: ")

    for order in order_list:
        if order["id"] == order_id:
            print("\n===== ORDER STATUS =====")
            print(f"Order ID: {order['id']}")
            print(f"Current Status: {order['status']}")

            current_index = order_status.index(order["status"])

            if current_index < len(order_status) - 1:
                order["status"] = order_status[current_index + 1]
                print(f"Updated Status: {order['status']}")
            else:
                print("Order has already been delivered.")

            return

    print("Order not found.")


# ============================================================
# USER FOOD ORDERING
# ============================================================

def browse_restaurants():
    print("\n===== BROWSE RESTAURANTS =====")
    view_restaurants()


def view_menu():
    view_restaurants()

    restaurant = input("\nEnter restaurant name: ")

    found = False

    print(f"\n===== MENU: {restaurant} =====")

    for food in food_list:
        if food["restaurant"].lower() == restaurant.lower():
            print(
                f"{food['name']} - ₹{food['price']}"
            )
            found = True

    if not found:
        print("No food items found.")


def add_to_cart():
    view_food_items()

    if not food_list:
        return

    try:
        number = int(input("\nEnter food item number: ")) - 1

        if 0 <= number < len(food_list):

            selected_food = food_list[number]

            cart_list.append(selected_food)

            print(
                f"{selected_food['name']} added to cart!"
            )

        else:
            print("Invalid food item.")

    except ValueError:
        print("Please enter a valid number.")


def show_cart():
    print("\n===== YOUR CART =====")

    if not cart_list:
        print("Cart is empty.")
        return

    total = 0

    for i, item in enumerate(cart_list, start=1):
        print(
            f"{i}. {item['name']} - "
            f"₹{item['price']}"
        )
        total += item["price"]

    print(f"\nTotal: ₹{total}")


def remove_from_cart():
    show_cart()

    if not cart_list:
        return

    try:
        index = int(input("\nEnter item number to remove: ")) - 1

        if 0 <= index < len(cart_list):

            # Python list pop()
            removed = cart_list.pop(index)

            print(f"{removed['name']} removed from cart.")

        else:
            print("Invalid number.")

    except ValueError:
        print("Invalid input.")


def place_order():
    if not cart_list:
        print("Your cart is empty.")
        return

    show_cart()

    username = input("\nEnter your username: ")
    address = input("Enter delivery address: ")

    if not username or not address:
        print("Username and address are required.")
        return

    restaurants = []

    for item in cart_list:
        if item["restaurant"] not in restaurants:
            restaurants.append(item["restaurant"])

    total = sum(item["price"] for item in cart_list)

    order_id = f"ORD{len(order_list) + 1:03d}"

    order = {
        "id": order_id,
        "user": username,
        "restaurant": ", ".join(restaurants),
        "items": [item["name"] for item in cart_list],
        "total": total,
        "address": address,
        "status": "Placed"
    }

    # Python list append()
    order_list.append(order)

    # Clear cart after placing order
    cart_list.clear()

    print("\n===== ORDER PLACED =====")
    print(f"Order ID: {order_id}")
    print(f"Total Amount: ₹{total}")
    print("Status: Placed")
    print("Your food will be delivered soon!")


def order_history():
    username = input("Enter your username: ")

    print("\n===== ORDER HISTORY =====")

    found = False

    for order in order_list:
        if order["user"].lower() == username.lower():
            print(f"\nOrder ID: {order['id']}")
            print(f"Items: {', '.join(order['items'])}")
            print(f"Total: ₹{order['total']}")
            print(f"Status: {order['status']}")
            found = True

    if not found:
        print("No previous orders found.")


# ============================================================
# REPORTS
# ============================================================

def reports():
    print("\n===== REPORTS =====")

    print(f"Total Restaurants : {len(restaurant_list)}")
    print(f"Total Food Items  : {len(food_list)}")
    print(f"Total Users       : {len(user_list)}")
    print(f"Total Orders      : {len(order_list)}")

    total_sales = 0

    for order in order_list:
        total_sales += order["total"]

    print(f"Total Sales       : ₹{total_sales}")


# ============================================================
# OWNER DASHBOARD
# ============================================================

def owner_dashboard():
    while True:
        print("\n")
        line()
        print("              OWNER PANEL")
        line()

        print("1. Dashboard")
        print("2. Manage Restaurants")
        print("3. Manage Food Items")
        print("4. View Orders")
        print("5. Manage Users")
        print("6. Reports")
        print("7. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            reports()
            pause()

        elif choice == "2":
            manage_restaurants()

        elif choice == "3":
            manage_food_items()

        elif choice == "4":
            view_orders()
            pause()

        elif choice == "5":
            manage_users()

        elif choice == "6":
            reports()
            pause()

        elif choice == "7":
            print("Owner logged out successfully.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# USER PANEL
# ============================================================

def user_panel():
    while True:
        print("\n")
        line()
        print("               USER PANEL")
        line()

        print("1. Browse Restaurants")
        print("2. View Menu")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Remove from Cart")
        print("6. Place Order")
        print("7. Track Order")
        print("8. Order History")
        print("9. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            browse_restaurants()
            pause()

        elif choice == "2":
            view_menu()
            pause()

        elif choice == "3":
            add_to_cart()

        elif choice == "4":
            show_cart()
            pause()

        elif choice == "5":
            remove_from_cart()

        elif choice == "6":
            place_order()
            pause()

        elif choice == "7":
            track_order()
            pause()

        elif choice == "8":
            order_history()
            pause()

        elif choice == "9":
            print("User logged out successfully.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    while True:
        print("\n")
        line()
        print("       FOOD ORDERING MANAGEMENT SYSTEM")
        line()

        print("Delicious Food, Delivered Fast!\n")

        print("1. Owner Panel")
        print("2. User Panel")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            owner_dashboard()

        elif choice == "2":
            user_panel()

        elif choice == "3":
            print("\nThank you for using Food Ordering Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Program starts here
if __name__ == "__main__":
    main()
