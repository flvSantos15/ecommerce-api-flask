from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# config of db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

# start of the db
db = SQLAlchemy(app)

# Modelagem
# Produto (id, name, price, description)

# Definition of the table product
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  price = db.Column(db.Float, nullable=False)
  description = db.Column(db.Text, nullable=False)


@app.route('/api/products/add', methods=['POST'])
def add_product():
  data = request.json
  if 'name' in data and 'price' in data:
    product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added sucessfully!"})
  return jsonify({"message": "Invalid product data"}), 400


@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
  product = Product.query.get(product_id)
  if product:
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted sucessfullly!"})
  return jsonify({"message": "Product not found!"}), 404

# route definition
@app.route('/')
def hello_world():
  return 'Hello world'

# debug is only used in develop enviroment
if __name__ == "__main__":
  app.run(debug=True)
