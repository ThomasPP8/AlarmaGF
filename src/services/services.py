from flask import request, jsonify

from config.mongodb import mongo

# Funcion para crear registros

def create_registro():
    data = request.get_json()
    titulo = data.get('titulo', None)
    valor = data.get('valor')
    estado = data.get('estado')
    if valor or estado:
        response = mongo.db.registros.insert_one({
            'titulo': titulo,
            'valor': int(valor),
            'estado': estado
        })
        result = {
            'id': str(response.inserted_id),
            'titulo': titulo,
            'valor': valor, 
            'estado': estado
        }
        return jsonify(result), 201
    else:
        return jsonify({"error": "faltan datos"}), 400