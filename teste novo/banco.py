from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dados simulados como um dicionário
products_data = []

@app.route('/')
def index():
    return render_template('index.html')  # Substitua pelo caminho correto para o seu arquivo HTML

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    products_data.append(data)
    return jsonify(success=True)

@app.route('/get_products', methods=['GET'])
def get_products():
    return jsonify(products_data)

@app.route('/update_product', methods=['POST'])
def update_product():
    data = request.json
    product_id = data['id']
    products_data[product_id] = data
    return jsonify(success=True)

@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    del products_data[product_id]
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
