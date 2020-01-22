from flask import Flask, jsonify, abort, request
app = Flask(__name__)
PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Bein.tv' }
]
PRODUCTS_COUNT = 3


@app.route('/api/v1/products')
def hello():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>',methods=['GET'])
def get_id_name(id):
    for product in PRODUCTS:
        if product['id'] == id:
            return product
    abort(404)

@app.route('/api/v1/products/<int:id>',methods=['DELETE'])
def delete_name(id):
    for product in PRODUCTS:
        if product['id'] == id:
            PRODUCTS.remove(product)
            return "",204
    abort(404)

@app.route('/api/v1/products',methods=['POST'])
def post_product():
    data = request.get_json()
    if not data['name'] :
        abort(400)
    new_product = {'id': PRODUCTS[-1]['id']+1,'name':data['name']}
    PRODUCTS.append(new_product)

    return new_product , 201

