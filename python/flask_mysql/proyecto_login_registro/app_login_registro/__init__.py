from flask import Flask

app = Flask(__name__)
DATA_BASE='user'
app.secret_key = "clave_secreta"