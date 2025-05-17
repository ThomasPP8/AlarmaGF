from flask import request, jsonify, Response
from bson import json_util, ObjectId

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

# Funcion para obtener todos los registros
def get_all_registros():
    data = mongo.db.registros.find()
    result = json_util.dumps(data) # Convertir a JSON
    return Response(result, mimetype='application/json') # Devolver la respuesta como JSON
    #return result, 200
    
# Funcion para obtener un registro por id
def get_registro_by_id(id):
    data = mongo.db.registros.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(data) # Convertir a JSON
    return Response(result, mimetype='application/json') # Devolver la respuesta como JSON