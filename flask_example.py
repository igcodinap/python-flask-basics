from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
# Flask(flask_example)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/itemsDB'

db = SQLAlchemy(app)

items_db = {}
#{'1': { id: 1, name: xxxxx}, '2': { id: 2, name: xxxxx}, '3': { id: 3, name: xxxxx}}

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

# @app.route('/items', methods=['POST'])
# def create_item():
#     print(request.json)
#     item = {
#         'id': str(len(items_db) + 1 ),
#         'name': request.json['name'],
#     }
#     items_db[item['id']] = item
#     return jsonify(item), 203

@app.route('/items', methods=['POST'])
def create_item():
    newItem = Item(name=request.json['name'])
    db.session.add(newItem)
    # db.session.add(newUser)
    # db.session.add(newWallet)
    db.session.commit()
    return jsonify(newItem.serialize()), 201

@app.route('/', methods=['GET'])
def hello_world():
    greeting = 'hola mundo'
    return greeting

# CRUD

#ruta para GET
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items_db.values()))


@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id not in items_db:
        abort(404)
    return jsonify(items_db[item_id])

# PUT
@app.route('/items/<string:item_id>', methods=['PUT'])
def update_item(item_id):
    if 'name' not in request.json:
        return abort(400)
    if item_id not in items_db:
        abort(404)
    items_db[item_id]['name'] = request.json['name']
    return jsonify(items_db[item_id]), 200

# DELETE
@app.route('/items/<string:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items_db:
        abort(404)
    deleted_item = items_db.pop(item_id)
    print(deleted_item)
    return jsonify({'result': 'success', 'deleted': deleted_item})

if __name__ == '__main__':
    app.run(port=8000)