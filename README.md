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


# 🛠️ Refactoring Lab

Цей проєкт створений у рамках лабораторної роботи з програмного забезпечення. Метою є застосування принципів **SOLID**, патернів проєктування, написання модульних тестів, а також використання **SonarQube** для аналізу якості коду.

## 🔍 Зміст

- [Про проєкт](#про-проєкт)
- [Використані технології](#використані-технології)
- [Функціональність](#функціональність)
- [Архітектура та патерни](#архітектура-та-патерни)
- [Як запустити](#як-запустити)
- [Аналіз коду з SonarQube](#аналіз-коду-з-sonarqube)
- [Тестування](#тестування)
- [Автор](#автор)

---

## 📌 Про проєкт

Проєкт демонструє:

- використання принципів **SOLID**;
- шаблони проєктування (**Singleton**, **Factory**, **Observer**);
- написання модульних тестів із використанням `unittest`;
- рефакторинг початкової версії програми;
- аналіз якості коду за допомогою **SonarQube**.

---

## 💻 Використані технології

- Python 3.10+
- `unittest` для тестування
- Git + GitHub
- SonarCloud (SonarQube)
- PEP8 code style

---

## ⚙️ Функціональність

- Реєстрація та обробка замовлень
- Класи для клієнтів та замовлень
- Валідація даних
- Реалізація бізнес-логіки через патерни проєктування
- Звіт про якість коду в SonarQube

---

## 🚀 Як запустити

```bash
# Клонування проєкту
git clone https://github.com/galaburdal/refactoring_lab.git
cd refactoring_lab

# Запуск основного коду
python main.py
```

---

## 📊 Аналіз коду з SonarQube

Проєкт підключено до [SonarCloud](https://sonarcloud.io/project/overview?id=galaburdal_refactoring_lab), де автоматично аналізується:

- дублікація коду
- code smells
- покриття тестами
- потенційні баги

---

## ✅ Тестування

Тести знаходяться в директорії `tests/`. Для запуску:

```bash
python -m unittest discover -s tests
```

---

## 👤 Автор

**Лабораторна робота з ПЗ**  
Автор: [@galaburdal](https://github.com/galaburdal)  
Дата: Квітень 2025



