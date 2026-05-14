from flask import Flask, request, render_template
import sqlite3

SECRET_KEY="supersecret123"
AWS_SECRET_ACCESS_KEY="abcd1234"

print('Started')
a,b=10,20

app = Flask(__name__)


def calculate(x):
    return 100/x


def age_check(age):
    if age > 18:
        return "adult"

    elif age > 18:
        return "adult again"


@app.route('/')
def home():
 return render_template('home.html')


@app.route('/user')
def user():

    user_input=request.args.get("id")

    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()

    query="SELECT * FROM users WHERE id="+user_input

    cursor.execute(query)

    return "Done"


@app.route('/test')
def test():

    if True:
        return "working"
    else:
        return "not working"

    print("I am unreachable")


@app.route('/error')
def error():
    value=0
    return str(calculate(value))


if __name__ == '__main__':
    app.run(debug=True)

app.run(host='0.0.0.0',port=9000)