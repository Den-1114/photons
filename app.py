from flask import Flask, redirect, render_template, request, jsonify, url_for, session
from flask_session import Session
import os

with open('password.key', 'r') as f:
    password = f.read()
    print(password)

app = Flask(__name__)
app.config["SECRET_KEY"] = 'sdgfcfdcgds'
app.config["SESSION_TYPE"] = 'filesystem'  # Correct session type configuration
Session(app)

# Get the path to the static/images folder
path = os.path.dirname(os.path.abspath(__file__)) 
path = os.path.join(path, 'static', 'images')
print(path)

# List all files in static/images
list_of_files = os.listdir(path)
print(list_of_files)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password_ = request.form['password']
        if password_ == password:
        # For now, just simulate a login by setting the session key
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return redirect(url_for('error'))
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/error', methods=['GET', 'POST'])
def error():
    return redirect(url_for('login'))

@app.route('/')
def index():
    # Check if 'logged_in' is in session to avoid KeyError
    if session.get('logged_in'):
        list_of_files = os.listdir(path)
        return render_template('index.html', files=list_of_files)
    else:
        return redirect(url_for('error'))

@app.route('/add_images', methods=['GET', 'POST'])
def add_images():
    if session.get('logged_in'):
        if request.method == 'GET':
            return render_template('add_a_file.html')
        elif request.method == 'POST':
            # Get the uploaded file from the form
            file = request.files['photo']
            if file and file.filename != '':
                # Save the file to the static/images folder
                file.save(os.path.join(path, file.filename))
            return redirect(url_for('index'))
        
    else:
        return redirect(url_for('error'))
