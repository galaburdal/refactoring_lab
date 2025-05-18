from run.coffee.factory import CoffeeFactory
from run.decorators.decorators import Milk, Syrup, WhippedCream
from run.commands.order import Order
from run.commands.place_order import PlaceOrderCommand
from run.commands.cancel_order import CancelOrderCommand
from run.order_manager import OrderManager
import os, time

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def pause():
    input("\nНатисніть Enter, щоб продовжити...")

def main():
    manager = OrderManager()
    factory = CoffeeFactory()

    while True:
        clear_screen()
        print("="*40)
        print("☕  Coffee Order System  ☕".center(40))
        print("="*40)
        print("1) Нове замовлення")
        print("2) Показати поточні замовлення")
        print("3) Скасувати останнє замовлення")
        print("4) Вихід")
        print("="*40)
        choice = input("Ваш вибір: ").strip()

        if choice == '1':
            clear_screen()
            print("-- Вибір напою --")
            for i,(name,price) in enumerate([("Espresso",2.00),("Latte",3.50),("Americano",2.50),("Cappuccino",3.00)], start=1):
                print(f"{i}. {name} (${price:.2f})")
            sel = input("Номер: ").strip()
            types = {'1':'espresso','2':'latte','3':'americano','4':'cappuccino'}
            coffee = factory.create_coffee(types.get(sel,'espresso'))

            print("\n-- Додати інгредієнти --")
            print("1. Milk (+$0.50)")
            print("2. Syrup (+$0.30)")
            print("3. Whipped Cream (+$0.70)")
            print("Введіть номери через кому, або Enter для пропуску.")
            for ing in input("Ваш вибір: ").split(','):
                if ing.strip() == '1': coffee = Milk(coffee)
                elif ing.strip() == '2': coffee = Syrup(coffee)
                elif ing.strip() == '3': coffee = WhippedCream(coffee)

            order = Order(coffee.get_description(), coffee.get_cost())
            manager.execute_command(PlaceOrderCommand(manager, order))
            print(f"\n✅ Ви замовили: {order}")
            pause()

        elif choice == '2':
            clear_screen()
            manager.list_orders()
            pause()

        elif choice == '3':
            clear_screen()
            manager.undo_last()
            pause()

        elif choice == '4':
            print("\n👋 Дякуємо за замовлення!")
            time.sleep(1)
            break

        else:
            print("⚠ Невірний вибір, спробуйте ще раз.")
            pause()

if __name__ == "__main__":
    main()
