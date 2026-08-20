from flask import Flask
from routes.usuarios_routes import usuarios_routes

app = Flask(__name__)

app.register_blueprint(usuarios_routes)

if __name__ == "__main__":
    app.run(debug=True)