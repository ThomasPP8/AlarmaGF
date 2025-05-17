from flask import Flask, render_template

from routes.registros import registros_bp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

app.register_blueprint(registros_bp, url_prefix='/registros')

if __name__=="__main__":
    app.run(debug=True)