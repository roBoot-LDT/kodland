from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime, timedelta
from random import randint
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)

app.config.update(
    SECRET_KEY = 'WOW SUCH SECRET'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(login):
    if login == 'admin':
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
    product = [{'name': 'Супер крутой товар',
                 'description': 'Это супер крутой товар, скорее покупай', 
                 'price':50, 
                 'img':'/static/images/2.jpg'},
                 {'name': "test",
                 'description': 'sth',
                 'price': 100,
                 'img':"/static/images/1.jpg'"}]
    return render_template('products.html', product=product)

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
    date = datetime.strptime('2022.12.25', '%Y.%m.%d')
    delta = date - datetime.now()
    days_before_end = delta.days
    end_date = datetime.now() + timedelta(days=14)
    end_date = end_date.strftime('%d.%m.%Y')
    return render_template('product1.html', action_name='Весенние скидки', end_date=end_date, days_before_end=days_before_end, number=10)

@app.route('/product2')
@login_required
def product2():
    return render_template('product2.html')

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

@app.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    if request.method == 'POST':
        for key in request.form:
            print(key, request.form[key])
            if request.form[key] == '':
                return render_template('order.html', error='Не все поля заполнены!')
    return render_template('order.html')

@app.route('/order_list')
@login_required
def order_list():
    return render_template('order_list.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    login = 'admin'
    password = 'admin'
    if request.method == 'POST':
        if request.form['login'] == login and request.form['password'] == password:
            user = User(login) # Создаем пользователя
            login_user(user) # Логинем пользователя
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Неправильный логин или пароль')
    return render_template('login.html')

@app.route("/logout")
def logout():
    logout_user()
    return "Пока!"

if __name__ == "__main__":
    app.run()
