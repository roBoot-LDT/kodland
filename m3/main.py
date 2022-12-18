from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/contacts')
def contacts():
    return 'Контакты'

@app.route('/about')
def about():
    return 'О компании'

@app.route("/cart")
def cart():
    return render_template("cart.html")
    
if __name__ == "__main__":
    app.run()
