from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy 
import json

# Flask(flask_example)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/itemsDB'

db = SQLAlchemy(app)

items_db = {}
#{'1': { id: 1, name: xxxxx}, '2': { id: 2, name: xxxxx}, '3': { id: 3, name: xxxxx}}

class Item(db.Model): # class Item extends db.Model
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True) # 1
    name = db.Column(db.String(30)) # test 1
    def serialize1(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def serialize2(self): 
        return {
            'name': self.name,
        }

@app.route('/items', methods=['POST'])
def create_item():
    newItem = Item(name=request.json['name'])

    db.session.add(newItem)
    db.session.commit()
    return jsonify(newItem.serialize1()), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all() # SELECT * FROM items
    return jsonify([item.serialize1() for item in items])

@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id) # SELECT * FROM items WHERE id=item_id
    if item is None:
        abort(404)
    return jsonify(item.serialize1())

@app.route('/items/<string:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        abort(404)
    print((item.__dict__))
    item.name = request.json['name']
    print(item.__dict__)
    db.session.commit()
    return (jsonify(item.serialize1()))

@app.route('/items/<string:item_id>', methods = ['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    print(item.__dict__)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'result': 'success'})
    


############### old CRUD - soon gonna be eliminated #####################

# @app.route('/items', methods=['POST'])
# def create_item():
#     print(request.json)
#     item = {
#         'id': str(len(items_db) + 1 ),
#         'name': request.json['name'],
#     }
#     items_db[item['id']] = item
#     return jsonify(item), 203

# @app.route('/items', methods=['GET'])
# def get_items():
#     return jsonify(list(items_db.values()))

#@app.route('/items/<string:item_id>', methods=['GET'])
# def get_item(item_id):
#     if item_id not in items_db:
#         abort(404)
#     return jsonify(items_db[item_id])

# PUT
# @app.route('/items/<string:item_id>', methods=['PUT'])
# def update_item(item_id):
#     if 'name' not in request.json:
#         return abort(400)
#     if item_id not in items_db:
#         abort(404)
#     items_db[item_id]['name'] = request.json['name']
#     return jsonify(items_db[item_id]), 200

# DELETE
# @app.route('/items/<string:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     if item_id not in items_db:
#         abort(404)
#     deleted_item = items_db.pop(item_id)
#     print(deleted_item)
#     return jsonify({'result': 'success', 'deleted': deleted_item})

if __name__ == '__main__':
    app.run(port=8000)





# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30))
#     lastname = db.Column(db.String(30))
#     email =  db.Column(db.String(30))
#     password =  db.Column(db.String(30))

#     def printer(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'lastname': self.lastname,
#             'email': self.email
#         }
    
#     def printer_inner(self):
#         return {
#             'id': self.id,
#             'email': self.email,
#             'password': self.password
#         }
    



# @app.route('/users/<string:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get(user_id) # SELECT * FROM users WHERE id=user_id
#     if user is None:
#         abort(404)
#     return jsonify(user.printer())

# @app.route('/protectedroute/users/<string:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get(user_id) # SELECT * FROM users WHERE id=user_id
#     if user is None:
#         abort(404)
#     return jsonify(user.printer_inner())
