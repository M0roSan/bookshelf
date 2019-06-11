from flask import Flask


app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/hi/<name>')
def say_hi(name):
    return f'Hello, {name}!'

@app.route('/age/<int:age>')
def show_age(age):
    return f'Age is {age}'


if __name__ == '__main__':
    app.run(debug=True)