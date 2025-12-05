from flask import Flask
# import redis



app = Flask(__name__)
# redis_obj = redis.Redis(host='redis', port=6379)

@app.route('/')
def base():
    # redis_obj = redis()
    print('Running AWS')
    # count = redis_obj.incr('counter')
    return f'Hello AWS '

app.run(host='0.0.0.0',port=9000)