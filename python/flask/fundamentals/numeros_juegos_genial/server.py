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
        elif 'num_azar' in session:
            if session['count'] > 0 and session['count']<= 4:
                print("la session ya existe")
            elif session['count'] > 4 and session['resultado'] != 'igual':
                session['resultado'] = "perdiste"
        print(session['num_azar'])
        return render_template("index.html")


@app.route('/guess', methods=['POST'])         
def guess():
        numero_ingresado = int(request.form['numero'])
        print(numero_ingresado)
        if session['num_azar'] == numero_ingresado:
                session['resultado'] = "igual"
                print('paso por igual')
        elif session['num_azar'] > numero_ingresado:
                session['resultado'] = "mayor"
                print('paso por mayor')
        elif session['num_azar'] < numero_ingresado:
                session['resultado'] = "menor"
                print('paso por menor')  
        session['count'] += 1 
        return redirect('/')

@app.route('/play_again', methods=['POST'])
def play_again():
    session.pop('num_azar')
    session.pop('resultado')
    session.pop('count')

    return redirect('/')

@app.route('/ranking', methods=['POST'])
def ranking():
    print(session['ranking'])
    if 'ranking' not in session:
        session['ranking'] = []
        
    session['ranking'] = [
        dict(nombre=request.form['nombre'], intentos=session['count'])]
    print(request.form['nombre'])
    print(session['ranking'])
    return render_template("ranking.html", ranking=session['ranking'])



if __name__=="__main__":   
    app.run(debug=True)