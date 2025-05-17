from flask import Flask, render_template
from dotenv import load_dotenv
import os

from config.mongodb import mongo
from routes.registros import registros_bp

config = load_dotenv() # Cargar variables de entorno desde el archivo .env

app = Flask(__name__) # Configurar la aplicación Flask

app.config['MONGO_URI'] = os.getenv('MONGO_URI') # Configurar la URI de MongoDB desde las variables de entorno
mongo.init_app(app) # Inicializar la conexión a MongoDB

@app.route('/') # Ruta principal
def home(): # Renderizar la plantilla index.html
    return render_template('index.html')

app.register_blueprint(registros_bp, url_prefix='/registros') # Registrar el blueprint de registros

if __name__=="__main__": # Ejecutar la aplicación
    app.run(debug=True)