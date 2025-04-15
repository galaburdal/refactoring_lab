# 📑 Лабораторна робота 4

## 🌐 Опис проєкту
**Тема:** Система створення замовлень з меню доставки їжі

**Мета:** Створити систему за принципами SOLID, з TDD-підходом та застосуванням шаблонів проектування (Singleton, Factory, Observer).

## 🌐 Структура проєкту
```
lab4/
├── models/                  # Основні класи системи
├── patterns/                # Шаблони проектування
├── main.py                  # Тестовий інтерфейс
├── test_lab4.py             # Юніт-тести
```

## 🔧 Застосовані принципи та шаблони
- **SOLID:** Всі класи мають одну відповідальність, розєднані через інтерфейси.
- **Singleton:** `OrderDatabase` — єдиний екземпляр бази.
- **Factory:** `StandardOrderFactory` — створює різні типи `Order`
- **Observer:** `OrderObserver` + `KitchenNotifier` — оповіщення кухні

---

## 🔢 Опис головних класів та методів

### models/dish.py
```python
class Dish:
    def __init__(self, name, price):
        self.name = name       # Назва страви
        self.price = price     # Ціна страви
```

### models/menu.py
```python
class Menu:
    def add_dish(self, dish):
        '''Додає страву до меню'''

    def get_dishes(self):
        '''Повертає список всіх страв'''
```

### models/client.py
```python
class Client:
    def add_order(self, order):
        '''Додає замовлення клієнту'''

    def get_orders(self):
        '''Отримує список замовлень'''
```

### models/order.py
```python
class Order:
    def add_dish(self, dish):
        '''Додає страву до замовлення'''

    def get_total(self):
        '''Рахує суму за замовлення'''
```

---

## ✅ Результати тестів (`test_log.md`)

### Проведено 10 тестів:
| Тест                               | Результат       |
|--------------------------------------|-------------------|
| test_add_dish_to_menu                | Успішно         |
| test_create_client                   | Успішно         |
| test_order_total                     | Успішно         |
| test_attach_observer                 | Успішно         |
| test_order_database_singleton        | Успішно         |
| test_add_order_to_database           | Успішно         |
| test_create_order_via_factory        | Успішно         |
| test_add_order_to_client             | Успішно         |
| test_empty_menu                      | Успішно         |
| test_dish_creation                   | Успішно         |

🌟 **100% проходження тестів!**

---

## 📅 Висновок
- Систему спроектовано відповідно до SOLID.
- Реалізовано 3 класичні шаблони: Singleton, Factory, Observer.
- Всі основні компоненти тестовані.
- Код якісний, чистий і структурований.

---




