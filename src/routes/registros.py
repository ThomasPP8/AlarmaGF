from flask import Blueprint
#from services.services import create_registro, get_all_registros, get_registro_by_id, update_registro
from services.services import (
    create_registro,
    get_all_registros,
    get_registro_by_id,
    update_registro,
    delete_registro
)

registros_bp = Blueprint('registros', __name__)

# Obtener todos los registros
@registros_bp.route('/', methods=['GET'])
def obtener_todos_los_registros():
    return get_all_registros()

# Obtener un registro por id
@registros_bp.route('/<id>', methods=['GET'])
def obtener_registro_por_id(id):
    return get_registro_by_id(id)

# Crear un registro
@registros_bp.route('/', methods=['POST'])
def crear_registro():
    return create_registro()

# Actualizar registro
@registros_bp.route('/<id>', methods=['PUT'])
def actualizar_registro(id):  # <- aquí se añadió `id`
    return update_registro(id)

# Eliminar registro
@registros_bp.route('/<id>', methods=['DELETE'])
def eliminar_registro(id):  # <- aquí también
    return delete_registro(id)
