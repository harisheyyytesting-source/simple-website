from flask import Flask, render_template
# import redis



app = Flask(__name__)
# redis_obj = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/portal')
def portal():
    return render_template('portal.html')


if __name__ == '__main__':
    app.run(debug=True)

app.run(host='0.0.0.0',port=9000)