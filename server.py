from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run('0.0.0.0', debug=True)