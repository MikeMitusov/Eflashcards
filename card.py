import json


def call_to_data(): # Remove this soon
    try:
        with open("data.json", "r") as f:
            global data
            data = json.load(f)
    except Exception:
        data = {}


call_to_data()


class Card:
    def add_card(self, group, front_text, back_text):
        if group not in data:
            data[group] = {}

        data[group][front_text] = back_text

    def save(self):
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
