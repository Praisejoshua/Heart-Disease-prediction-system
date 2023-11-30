from flask import Flask, render_template, request, redirect, url_for, session, flash,jsonify
# from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
import pandas as pd


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database creation
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    port = 3307,
    database = "healthcare_login"
)
cursor = db.cursor()

# database tables 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
               id INT AUTO_INCREMENT PRIMARY KEY,
               username VARCHAR(80) NOT NULL UNIQUE,
               password VARCHAR(120) NOT NULL,
               phone VARCHAR(20) NOT NULL,
               sex VARCHAR(10) NOT NULL
    )
""")
db.commit()

data = pd.read_csv("data/heart_failure_clinical_records_dataset.csv")
features = ['anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking']
target = 'age'

X1 = data[features]
y1 = data[target]

# spliting the data sent to test and train
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

# Home page
@app.route("/home")
def home_page():
        # flash("welcome")
        return render_template("home.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")
@app.route('/predict', methods= ["POST"])
def predict():
    if request.method == "POST":
        data_h = request.json #data sent with from the user which will be in a json format
        new_heart = pd.DataFrame(data_h, index=[0]) #data_h assumes to become a single data and is put in the first dataframe row
        predicted_age = model.predict(new_heart)
        return jsonify({'predicted_age': predicted_age[0]})
    
@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # excute queries
        cursor.execute("SELECT*FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session['username'] = username[0] #make sure that the user is authirized to stay
            # flash("Login successful")
            return redirect(url_for('home_page'))
        else:
            return("invalid username or password")
    
    return render_template('login.html')
@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute('SELECT * FROM users WHERE username = %s',(username,))
        existing_user = cursor.fetchone() #checking for existing users
        if existing_user:
            return("username already exists")
        else:
            hashed_password = generate_password_hash(password, method="sha256")

            cursor.execute('INSERT INTO users (username, password)VALUES (%s, %s)', (username, hashed_password))
            db.commit()
            # flash('sign up successful')
            return redirect(url_for('login_page'))

    return render_template('register.html')

if __name__ == "__main__":
    app.run (debug=True)