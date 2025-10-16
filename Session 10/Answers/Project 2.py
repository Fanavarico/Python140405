# 🛒 Shopping Cart System

# Class Definitions
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name} | ${self.price} | Qty: {self.quantity}"


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def update_item(self, index, item):
        self.items[index] = item

    def delete_item(self, index):
        return self.items.pop(index)

    def show_items(self):
        for i, it in enumerate(self.items):
            print(f"{i} - {it}")

    def total_price(self):
        total = sum(i.price * i.quantity for i in self.items)
        print(f"Total = ${total}")


# Menu Function
def cart_menu():
    print("1| Add Item")
    print("2| Update Item")
    print("3| Delete Item")
    print("4| Show Items")
    print("5| Show Total Price")
    print("0| Exit")


# Main Program
cart = Cart()

cart_menu()
choice = int(input("Enter Your Choice: "))

while choice != 0:
    if choice == 1:
        data = input("Name Price Quantity : ").split()
        it = Item(data[0], data[1], data[2])
        cart.add_item(it)

    elif choice == 2:
        cart.show_items()
        index = int(input("Enter index to update: "))
        data = input("Name Price Quantity : ").split()
        it = Item(data[0], data[1], data[2])
        cart.update_item(index, it)

    elif choice == 3:
        cart.show_items()
        index = int(input("Enter index to delete: "))
        print("Deleted:", cart.delete_item(index))

    elif choice == 4:
        cart.show_items()

    elif choice == 5:
        cart.total_price()

    else:
        print("Invalid Choice!")

    cart_menu()
    choice = int(input("Enter Your Choice: "))