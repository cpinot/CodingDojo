from flask import Flask

app = Flask(__name__)
app.secret_key = "clave_secreta"
BASE_DATOS= "dojos_y_ninjas"