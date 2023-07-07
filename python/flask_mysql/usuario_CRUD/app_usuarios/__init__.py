from flask import Flask


app = Flask(__name__)
BASE_DATOS='user'
app.secret_name='clave_secreta'