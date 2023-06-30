from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)  
app.secret_key = 'JSaafE54!@#$%$#%^&*()_+'

@app.route('/')         
def index():
        if 'count' in session:
            session['count'] += 1
        else:
            session['count'] = 1 

        return render_template("index.html", count=session['count'])
@app.route('/mas2')         
def mas_dos():
        if 'count' in session:
            session['count'] += 2
        else:
            session['count'] = 2 

        return render_template("index.html", count=session['count'])
@app.route('/destroy_session')
def destroy_session():
    session.clear()

    return redirect('/')

@app.route('/numero', methods=['POST'])
def numero():
        num = int(request.form['num'])
        print(num)
        
        if 'count' in session:
                session['count'] += num
        else:
            session['count'] = num 

        return render_template("index.html", count=session['count'])



if __name__=="__main__":   
    app.run(debug=True)