from flask import Blueprint

registros_bp = Blueprint('registros', __name__)

# Obtener todos los registros
@registros_bp.route('/', methods=['GET'])
def obtener_todos_los_registros():
    return "todos los registros"

# Obtener un registro por id
@registros_bp.route('/<id>', methods=['GET'])
def obtener_registro_por_id(id):
    return f"Registro con ID: {id}"

# Crear un registro
@registros_bp.route('/', methods=['POST'])
def crear_registro():
    return "crear registro"

# Actualizar registro
@registros_bp.route('/<id>', methods=['PUT'])
def actualizar_registro(id):  # <- aquí se añadió `id`
    return f"actualizar registro con ID: {id}"

# Eliminar registro
@registros_bp.route('/<id>', methods=['DELETE'])
def eliminar_registro(id):  # <- aquí también
    return f"eliminar registro con ID: {id}"
