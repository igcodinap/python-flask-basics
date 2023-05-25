from flask import Flask, jsonify
app = Flask(__name__)
todos = [ { "label": "My first task", "done": False } ]
@app.route('/todos', methods=['GET'])
def hello_world():
    print(todos, 'todo')
    json_text = jsonify(todos)
    print(json_text, 'json')
    return json_text
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)