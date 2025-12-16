from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html.jinja2')

@app.route('/user')
@app.route('/user/<username>')
def user(username=None):
    return render_template('user.html.jinja2', name=username)

if __name__ == '__main__':
    app.run(debug=True)
