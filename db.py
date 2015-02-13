import pprint
from pymongo import MongoClient
pp = pprint.PrettyPrinter(indent=2)

client = MongoClient()
db = client.todos
todos = db.todos

todo = todos.find_one()
pp.pprint(todo)

todo = todos.find_one({'position': 1})
pp.pprint(todo)

for todo in todos.find():
    pp.pprint(todo)
