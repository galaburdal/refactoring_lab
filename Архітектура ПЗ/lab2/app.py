from flask import Flask, render_template, request, jsonify, redirect, url_for
from db import Database
from facade import RegistrationFacade, User, OrderFacade

app = Flask(__name__)
db = Database()
registration_facade = RegistrationFacade(db)
order_facade = OrderFacade(db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    username = data.get('username')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    if not all([username, email, phone, password]):
        return jsonify({"error": "All fields are required"}), 400

    user = User(username, email, phone, password)

    if registration_facade.register_user(user):
        return jsonify({"message": "User registered successfully!"}), 201
    else:
        return jsonify({"error": "Registration failed"}), 400

@app.route('/order')
def order_page():
    return render_template('order.html')

@app.route('/order_bike', methods=['POST'])
def order_bike():
    data = request.get_json()
    if not data or 'user_id' not in data or 'bike_type' not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_id = data['user_id']
    bike_type = data['bike_type']
    order_message = order_facade.place_order(user_id, bike_type)

    return jsonify({"message": order_message}), 200

if __name__ == '__main__':
    app.run(debug=True)
