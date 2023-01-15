import re
from random import randint
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from kodland_db import db

app = Flask(__name__)

all_orders = []

app.config.update(
    SECRET_KEY='WOW SUCH SECRET'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(login):
    return User(login)

class User(UserMixin):
    def __init__(self, id):
        self.id = id


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/products')
@login_required
def products():
    return render_template('products.html')


@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html')


@app.route('/contacts')
@login_required
def contacts():
    return render_template('contacts.html')


@app.route('/about')
@login_required
def about():
    return render_template('about.html')


@app.route('/product1')
@login_required
def product1():
    end_date = datetime.now() + timedelta(days=7)
    end_date = end_date.strftime('%d.%m.%Y')
    return render_template('product1.html',
                           action_name='Весенние скидки!',
                           end_date=end_date,
                           lucky_num=randint(1, 5))


@app.route('/product2')
@login_required
def product2():
    brands = ['Colla', 'Pepppssi', 'Orio', 'Macdak']
    return render_template('product2.html', brands=brands)


@app.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    if request.method == 'POST':
        for key in request.form:
            if request.form[key] == '':
                return render_template('order.html', error='Не все поля заполнены!')
            if key == 'email':
                if not re.match('\w+@\w+\.(ru|com)', request.form[key]):
                    return render_template('order.html', error='Неправильный формат почты')
            if key == 'phone_number':
                if not re.match('\+7\d{9}', request.form[key]):
                    return render_template('order.html', error='Неправильный формат номера телефона')
            else:
                all_orders.append(request.form)
    return render_template('order.html')


@app.route('/api/orders')
def api_orders():
    return jsonify(all_orders)


@app.route('/order_list')
@login_required
def order_list():
    return render_template('order_list.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        row = db.users.get('login', request.form['login'])
        if not row:
            return render_template('login.html', error='Неправильный логин или пароль')

        if request.form['password'] == row.password:
            user = User(login)  # Создаем пользователя
            login_user(user)  # Логинем пользователя
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Неправильный логин или пароль')
    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return 'Пока'


@app.route('/lootbox')
@login_required
def lootbox():
    num = randint(1, 100)
    if num < 50:
        chance = 50
    elif 50 < num < 95:
        chance = 45
    elif 95 < num < 99:
        chance = 4
    else:
        chance = 1
    return render_template('lootbox.html', chance=chance)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        for key in request.form:
            if request.form[key] == '':
                return render_template('register.html', message='Все поля должны быть заполнены!')
        if request.form['password'] != request.form['password_check']:
            return render_template('register.html', message='Пароли не совпадают')
        row = db.users.get('login', request.form['login'])
        if row:
            return render_template('register.html', message='Такой пользователь уже существует!')
        if row.email:
            return render_template('register.html', message='Такая почта уже существует!')
        if row.phone:
            return render_template('register.html', message='Такой телефон уже существует!')
        data = dict(request.form)
        data.pop('password_check')
        db.users.put(data=data)
        return render_template('register.html', message='Регистрация прошла успешно')   

    return render_template('register.html')


if __name__ == "__main__":
    app.run()
