from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os
import time

from config.mongodb import mongo
from routes.registros import registros_bp

# Cargar variables de entorno
load_dotenv()

# Configurar Flask
app = Flask(__name__)
CORS(app)

# Configurar MongoDB
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
print("MONGO_URI:", app.config['MONGO_URI'])  # SOLO PARA DEBUG

mongo.init_app(app)
try:
    mongo.cx.server_info()  # Esto forza conexión y lanza error si falla
    print(" Conexión a MongoDB exitosa.")
except Exception as e:
    print(" Error al conectar con MongoDB:", e)
    
print("mongo.db:", mongo.db)


# Inicializar SocketIO
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Ruta principal (puedes mantener el index.html si lo necesitas)
@app.route('/')
def home():
    time.sleep(1)
    return "API Flask WebSocket funcionando", 200


# Registrar rutas del blueprint
app.register_blueprint(registros_bp, url_prefix='/registros')

# Eventos WebSocket
@socketio.on('connect')
def on_connect():
    print("Cliente conectado")

@socketio.on('disconnect')
def on_disconnect():
    print("Cliente desconectado")

@socketio.on('mensaje_esp')
def on_mensaje(data):
    print("ESP32 envió:", data)

# Iniciar la app con WebSocket
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8080, allow_unsafe_werkzeug=True)