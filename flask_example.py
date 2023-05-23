from flask import Flask, request, jsonify, abort
# Flask(flask_example)
app = Flask(__name__)

items_db = {}
#{ id: x, name: xxxxx}

@app.route('/', methods=['GET'])
def hello_world():
    greeting = 'hola mundo'
    return greeting

# CRUD

#ruta para GET
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items_db.values()))

@app.route('/items', methods=['POST'])
def create_item():
    item = {
        'id': str(len(items_db) + 1 ),
        'name': request.json['name']
    }
    items_db[item['id']] = item
    return jsonify(item), 201

@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id not in items_db:
        abort(404)
    return jsonify(items_db[item_id])


if __name__ == '__main__':
    app.run(port=8000)