from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)  
app.secret_key = 'JSaafE54!@#$%$#%^&*()_+'

@app.route('/')      
def index():
        print("ingreso a la pagina")
        if 'gold' not in session:
            session['gold'] = 0
            session['action'] = ""
            session['actividades'] = []
        if 'count' not in session:
            session['count'] = 0
        return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    color = "green"
    session['count'] += 1
    print("ingreso a process_money")
    print(request.form)
    if request.form['action'] == 'farm':
        num_aleatorio = random.randint(1,20)
        session['gold'] += num_aleatorio
        session['actividades'] += [f"Obtuviste {num_aleatorio} oro desde farm! ({datetime.now()})"]
    elif request.form['action'] == 'cave':
        num_aleatorio = random.randint(1,10)
        session['gold'] += num_aleatorio
        session['actividades'] += [f"Obtuviste {num_aleatorio} oro desde cave! ({datetime.now()})"]
    elif request.form['action'] == 'house':
        num_aleatorio = random.randint(1,5)
        session['gold'] += num_aleatorio
        session['actividades'] += [f"Obtuviste {num_aleatorio} oro desde house! ({datetime.now()})"]
    elif request.form['action'] == 'casino':
        num_aleatorio = random.randint(-50,50)
        session['gold'] += num_aleatorio
        if num_aleatorio < 0:
                color = "red"
                session['actividades'] += [f"Perdiste {num_aleatorio} oro desde casino!({datetime.now()})"]
        else:
            session['actividades'] += [f"Obtuviste {num_aleatorio} oro desde casino!({datetime.now()})"]
        
    print(session['count'])
    print(session['gold'])
    print(session['actividades'])
    return render_template("index.html", color=color)


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)