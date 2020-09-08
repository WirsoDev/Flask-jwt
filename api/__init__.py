from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # load dotenv variables

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("secret-key")

# set up flask routes
from api.routes import mainBp

app.register_blueprint(mainBp)
