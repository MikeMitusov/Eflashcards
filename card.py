import json


try:
    with open("data.json", "r") as f:
        data = json.load(f)
except Exception:
    data = {}


class Card:
    def add_card(self, group, front_text, back_text):
        if group not in data:
            data[group] = {}

        data[group][front_text] = back_text

    def save(self):
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
