from models.menu import Menu
from models.dish import Dish
from models.client import Client
from patterns.order_factory import StandardOrderFactory
from patterns.order_database_singleton import OrderDatabase
from patterns.observer import OrderObserver
from models.kitchen_notifier import KitchenNotifier

def main():
    menu = Menu()
    db = OrderDatabase()
    factory = StandardOrderFactory()
    observer = OrderObserver()
    kitchen = KitchenNotifier()
    observer.attach(kitchen)

    client_name = input("Введіть ім'я клієнта: ")
    client = Client(client_name)

    while True:
        print("\n1. Додати страву до меню")
        print("2. Показати меню")
        print("3. Створити замовлення")
        print("4. Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Назва страви: ")
            price = float(input("Ціна: "))
            menu.add_dish(Dish(name, price))

        elif choice == "2":
            print("\nМеню:")
            for dish in menu.get_dishes():
                print(f"{dish.name} - {dish.price} грн")

        elif choice == "3":
            order = factory.create_order(client)
            print("\nВиберіть страви (введіть назви):")
            for dish in menu.get_dishes():
                print(f"{dish.name} - {dish.price} грн")
            selected = input("Через кому: ").split(", ")
            for dish in menu.get_dishes():
                if dish.name in selected:
                    order.add_dish(dish)

            client.add_order(order)
            db.add_order(order)
            observer.notify_all(order)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()





