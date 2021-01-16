import time

from flask import Flask, request, abort

app = Flask(__name__)

db = [
    {
        "text": "Hello",
        "time": time.time(),
        "name": "John"
    },
    {
        "text": "Hello, John",
        "time": time.time(),
        "name": "Bill"
    }
]
@app.route("/")
def hello():
    return "Fuck you asshole"

@app.route("/send", methods=['POST'])
def send_message():

    name = request.json.get('name')
    text = request.json.get('text')

    message = {
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)
    return { "ok": True}

@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return {"message": messages}

app.run()