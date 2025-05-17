from flask import request, jsonify

from config.mongodb import mongo

# Funcion para crear registros

def create_registro():
    data = request.get_json()
    valor = data.get('valor', None)
    estado = data.get('estado', None)
    if valor or estado:
        response = mongo.db.registros.insert_one({
            'valor': valor,
            'estado': estado
        })
        result = {
            id: int(response.inserted_id),
            'valor': valor, 
            'estado': estado
        }
        return result
    else:
        return jsonify({"error": "error datos"}), 400