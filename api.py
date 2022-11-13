import datetime
import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return({"msg": "Welcome home george! Go to '/posts' endpoint for the actual text result"})

@app.route('/posts')
def george_example():
    curent_time = datetime.datetime.now()
    return({
                "fname": "George", 
                "lname": "Njuacha", 
                "time": curent_time,
                "new_timer": time.time(), 
                "msg": "Automate all the things!"
            })