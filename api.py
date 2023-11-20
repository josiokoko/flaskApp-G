import datetime
import time
from flask import Flask, jsonify

app = Flask(__name__)


from faker import Faker
fake = Faker()

def random_sentence():
    return fake.sentence()


@app.route('/')
def home():
    current_time = datetime.datetime.now().strftime("%m/%d/%Y  %H:%M:%S")
    return {
        "greetings": "Welcome to Onyxquity Cloud Computing!",
        "available_endpoints": {
            "home": "localhost:5557/",
            "posts": "localhost:5557/posts",
            "person_age": "localhost:5557/posts/<person>/<int:age>",
            "person_id": "localhost:5557/post/<person>/<person_id>"
        },
        'time': current_time, 
        'random_phrase': random_sentence()
    }

@app.route('/posts/')
def postspage():
    curent_time = datetime.datetime.now()
    return({
                "course": "Cloud Computing", 
                "level": "Intermediate-to-advanced", 
                "time": curent_time,
                "new_timer": time.time(),
                'msg': 'DevOps trainning on steroid...' 
            })


@app.route('/posts/<person>/<int:age>')
def hello(person, age):
    response= jsonify({
        "person": "{} is {} years old!".format(person, age)
        })
    return response


@app.route('/post/<person>/<person_id>')
def person(person, person_id):
    response = jsonify({ 
        person + "_id" : person_id
    })
    return response 

