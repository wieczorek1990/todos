from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import pprint

pp = pprint.PrettyPrinter(indent=2)

app = Flask(__name__)
app.debug = True

client = MongoClient()
db = client.todos
todos = db.todos


def unpack(record):
    del record['_id']
    return record


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/")
def index():
    result = {}
    for todo in todos.find():
        position = todo['position']
        text = todo['text']
        result[str(position)] = text
    return jsonify(**result)


@app.route("/<position>")
def get(position):
    todo = todos.find_one({'position': int(position)})
    if todo is not None:
        del todo['_id']
        return jsonify(**todo)
    else:
        return jsonify(**{})

if __name__ == "__main__":
    app.run(debug=app.debug)
