import bcrypt
from db import Database
from builder import BikeBuilder

class User:
    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

class Validator:
    def validate_user(self, user: User) -> bool:
        if not user.username or not user.email or not user.phone or not user.password:
            print("Помилка: Всі поля повинні бути заповнені!")
            return False

        if "@" not in user.email:
            print("Помилка: Неправильний формат email!")
            return False

        if not user.phone.isdigit() or len(user.phone) < 10:
            print("Помилка: Невірний номер телефону!")
            return False

        print("Користувач успішно пройшов валідацію!")
        return True

class UserDataAccess:
    def __init__(self, db: Database):
        self.db = db

    def save_user(self, user: User) -> bool:
        hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
        return self.db.add_user(user.username, user.email, user.phone, hashed_password)

class EmailService:
    def send_registration_email(self, user: User):
        print(f"Відправлено email на {user.email} про успішну реєстрацію!")

class RegistrationFacade:
    def __init__(self, db: Database):
        self.validator = Validator()
        self.user_data_access = UserDataAccess(db)
        self.email_service = EmailService()

    def register_user(self, user: User) -> bool:
        if not self.validator.validate_user(user):
            return False

        if not self.user_data_access.save_user(user):
            print("Помилка: Не вдалося зберегти користувача в базу даних!")
            return False

        self.email_service.send_registration_email(user)
        print("Реєстрація пройшла успішно!")
        return True

class OrderFacade:
    def __init__(self, db: Database):
        self.db = db
        self.bike_builder = BikeBuilder()

    def place_order(self, user_id, bike_type):
        bike = self.bike_builder.build_bike(bike_type)
        if not self.db.add_order(user_id, bike.bike_type, bike.price):
            return "Помилка оформлення замовлення!"
        return f"Замовлення підтверджене: {bike}"
