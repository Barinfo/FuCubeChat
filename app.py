from flask import Flask
from blueprints import register_blueprints
from services.database_service import initialize_database
from utils.websocket_manager import socketio

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    
    register_blueprints(app)
    initialize_database(app)
    
    socketio.init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    socketio.run(app, debug=True)
