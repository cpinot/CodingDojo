from flask import Flask

app = Flask(__name__)
DATA_BASE='libros'
app.secret_key = "clave_secreta"