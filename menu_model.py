import json


def load_db():
    with open("recipe_list.JSON") as f:
        return json.load(f)


def save_db():
    with open("recipe_list.JSON", 'w') as f:
        return json.dump(db, f)


db = load_db()
