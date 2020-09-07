from flask import Flask
from dotenv import load_dotenv
import os
from api.routes import main_bp

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('secret-key')


app.register_blueprint(main_bp)
