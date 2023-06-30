from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fecha = datetime.now()
    suma= int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"Cobrando a {request.form['first_name']} {request.form['last_name']} for {suma} fruits")
    return render_template("checkout.html", suma=suma, fecha=fecha)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    