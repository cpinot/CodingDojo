from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)  
app.secret_key = 'JSaafE54!@#$%$#%^&*()_+'

@app.route('/')         
def index():
        #crear una variable session
        if 'num_azar' not in session:
            session['num_azar'] = random.randint(1,100)
            session['resultado'] = ""
            session['count'] = 0
            print(session['num_azar'])
        else:
            print("la session ya existe")
            print(session['num_azar']) 
        return render_template("index.html")


@app.route('/guess', methods=['POST'])         
def guess():
        print(request.form)
        session['count'] += 1
        numero_ingresado = int(request.form['numero'])
        if session['num_azar'] == numero_ingresado:
                session['resultado'] = "igual"
        elif session['num_azar'] > numero_ingresado and session['num_azar']:
                session['resultado'] = "mayor"
        elif session['num_azar'] < int(request.form['numero']):
                session['resultado'] = "menor"
        print(session['resultado'])
        return redirect('/')

@app.route('/play_again', methods=['POST'])
def play_again():
    session.clear()
    return redirect('/')



if __name__=="__main__":   
    app.run(debug=True)