# 🍕 Restaurant Order System

# Class Definitions
class Food:
    def __init__(self, name, price, flavor):
        self.name = name
        self.price = float(price)
        self.flavor = flavor

    def __str__(self):
        return f"{self.name} | {self.flavor} | ${self.price}"


class Order:
    def __init__(self):
        self.foods = []

    def add_food(self, food):
        self.foods.append(food)

    def update_food(self, index, food):
        self.foods[index] = food

    def delete_food(self, index):
        return self.foods.pop(index)

    def show_foods(self):
        for i, f in enumerate(self.foods):
            print(f"{i} - {f}")


# Menu Function
def order_menu():
    print("1| Add Food")
    print("2| Update Food")
    print("3| Delete Food")
    print("4| Show All Foods")
    print("0| Exit")


# Main Program
order = Order()

order_menu()
choice = int(input("Enter Your Choice: "))

while choice != 0:
    if choice == 1:
        data = input("Name Price Flavor : ").split()
        f = Food(data[0], data[1], data[2])
        order.add_food(f)

    elif choice == 2:
        order.show_foods()
        index = int(input("Enter index to update: "))
        data = input("Name Price Flavor : ").split()
        f = Food(data[0], data[1], data[2])
        order.update_food(index, f)

    elif choice == 3:
        order.show_foods()
        index = int(input("Enter index to delete: "))
        print("Deleted:", order.delete_food(index))

    elif choice == 4:
        order.show_foods()

    else:
        print("Invalid Choice!")

    order_menu()
    choice = int(input("Enter Your Choice: "))