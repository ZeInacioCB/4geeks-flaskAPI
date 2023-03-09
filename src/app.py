from flask import Flask, jsonify, request
app = Flask(__name__)

#When the application runs it will take over your command line, you will not be able to type on it anymore because a server application (like flask) never stops running, it keeps waiting for "requests" forever.
#What does this means? 
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def getTodos():
    todosJson = jsonify(todos)
    return todosJson

@app.route('/todos', methods=['POST'])
def add_new_todo():
    newTodo = request.json
    print("Incoming todo: ", newTodo)
    todos.append(newTodo)
    todos_json = jsonify(todos)
    return todos_json

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Deleting the following todo: ", todos[position])
    todos.pop(position)
    todos_json = jsonify(todos)
    return todos_json


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)