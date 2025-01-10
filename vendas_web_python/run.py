from flask import Flask, render_template, request, redirect, url_for, flash
import databases.user_database
from tkinter import messagebox

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Initial route
@app.route('/')
def index():
    return render_template('index.html')

# Route to login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        # Form submission
        username = request.form.get('username')
        password = request.form.get('password')

        database_user = databases.user_database.UserDatabase()
        user = database_user.authenticate_user('database_user',username, password)
        
        if user:
            return render_template('product.html')
            
        else:
            error_message = 'Usuário não autenticado!'
            message = error_message

    return render_template('login.html', error_message = message)

# Route to register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Form submission
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        # Display form data
        print(f"\n\nUsername: {username}, Password: {password}, Email: {email}\n\n")
        
        database_user = databases.user_database.UserDatabase()
        database_user.insert_user('database_user',username, password, email)

        # Redirect to the index page after submission
        flash('Registration successful', 'success')
        return render_template('product.html')

    return render_template('register.html')

# Runs and starts the Flask server
if __name__ == '__main__':
    app.run(debug=True)
