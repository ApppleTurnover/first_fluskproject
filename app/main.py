from flask import Flask, render_template, url_for, make_response, abort

app = Flask(__name__)

some_users = ['Athon', 'Apple', 'Greys', 'Jake']


@app.route('/')
def index():
    response = make_response('<h1>Some Text</h1>')
    response.set_cookie('answer', '41')
    return response


@app.route('/user/<user>')
def get_user(user):
    if user not in some_users:
        abort(404)
    return f'<h1>Hello, {user}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
