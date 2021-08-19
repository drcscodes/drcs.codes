from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<ul><li>Hello, Flask!</li><li>Hello, dolly!</li></ul>'

@app.route('/fun')
def fun():
    return 'Yippee!'

@app.route('/user/<fname>/<lname>')
def user(fname, lname):
    return f'<h1><i>Hello, {fname} {lname}!</i></h1>'

@app.route('/mybrowser')
def my_browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)
