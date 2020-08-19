from application import app
from flask import request, Response
from random import randint

@app.route('/animal/name', methods=['GET'])
def animal_name():
    animals = ['cat', 'dog', 'cow', 'duck']
    return Response(animals[randint(0,3)], mimetype='text/plain')

@app.route('/animal/noise', methods=['POST'])
def animal_noise():
    animal = request.data.decode("utf-8")
    if animal == "cat":
        noise = "meow"
    elif animal == "dog":
        noise = "woof"
    elif animal == "cow":
        noise = "moo"
    elif animal == "duck":
        noise = "quack"
    else:
        noise = "Noise is unknown"
    return Response(noise, mimetype='text/plain')
