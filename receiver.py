import time

import requests


def print_message(message):

    print(message['name'],':', message['text'])
    print()

def print_messages(db):
    for message in db:
        print_message(message)

after = 0
while True:
    response = requests.get(
            "http://127.0.0.1:5000/messages",
            params={'after': after}
        )
    messages = response.json()['message']
    for message in messages:
        print_message(message)
        after = message['time']

    time.sleep(2)