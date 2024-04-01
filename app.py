# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a secure Flask app!. I have made changes"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
