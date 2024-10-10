from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos), 201

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    try:
        removed_todo = todos.pop(index)
        return jsonify({'message': 'Todo deleted', 'removed': removed_todo}), 200
    except IndexError:
        return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
