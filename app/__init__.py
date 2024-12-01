from flask import Flask
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuración desde archivo de entorno
    app.config.from_object('config.Config')

    # Inicialización de Supabase
    app.supabase = create_client(
        os.getenv('SUPABASE_URL'),
        os.getenv('SUPABASE_KEY')
    )

    with app.app_context():
        from . import routes
        return app
