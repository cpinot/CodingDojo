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

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    session.pop('count')

    return render_template("index.html", count=session['count'])

if __name__=="__main__":   
    app.run(debug=True)    