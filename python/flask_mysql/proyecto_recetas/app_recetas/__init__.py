from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
DATA_BASE='recetas'
app.secret_key = "clave_secreta"