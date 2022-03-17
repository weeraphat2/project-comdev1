import email
from flask import Flask, render_template, request, flash, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'werty uiop'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template("login.html")

@app.route('/home', methods=['POST'])
def home():
    return render_template("home.html")


@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 7:
            flash('Email incomplete please try again.' ,category='error')
        elif len(name) < 1:
            flash('Enter your frist name  please try again.', category='error')
        elif password1 != password2:
            flash('Password not match please try again.', category='error' )
        elif len(password1) < 5:
            flash('Your password not safe please try again.', category='error' )
        else:
            flash('Signup success.', category='success' )

    return render_template("signup.html")

@app.route('/logout')
def logout():
    return render_template("/")

if __name__ == "__main__" :
    app.run(debug='true')