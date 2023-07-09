from flask import render_template, request, redirect, session
from app_recetas import app
from app_recetas.modelos.modelo_recipes import Recipes

@app.route('/recetas', methods=['GET'])
def desplegar_recetas():
    if 'usuario_id' in session:
        print(session['usuario_id'])
        obtener_recetas= Recipes.obtener_todas_las_recetas_con_usuarios()
        print(obtener_recetas)
        return render_template('recetas.html', recetas=obtener_recetas)
    else:
        return redirect('/login')
@app.route('/recetas/nueva', methods=['GET'])
def desplegar_crear_recetas():
    if 'usuario_id' in session:
        print(session['usuario_id'])
        return render_template('nueva_receta.html')
    else:
        return redirect('/login')
@app.route('/recetas/crear', methods=['POST'])
def crear_recetas():
    if 'usuario_id' in session:
        print(session['usuario_id'])
        print(request.form)
        if request.form['under_30_minutes'] == "Yes":
            under_30_minutes = True
        else:
            under_30_minutes = False
        data = {
            "name": request.form['name'],
            "description": request.form['description'],
            "instructions": request.form['instructions'],
            "under_30_minutes": under_30_minutes,
            "created_at": request.form['created_at'],
            "user_id": session['usuario_id']
        }
        validar_receta= Recipes.validar_receta(data)
        if validar_receta == False:
            return redirect('/recetas/nueva')
        else:
            nueva_receta= Recipes.crear_una_receta(data)
            print(nueva_receta)
            return redirect('/recetas')
    else:
        return redirect('/login')   
    
@app.route('/editar/receta/<int:id>', methods=['GET'])
def desplegar_editar_recetas(id):
    if 'usuario_id' in session:
        print(session['usuario_id'])
        data = {
            "id": id
        }
        receta= Recipes.obtener_una_receta(data)
        return render_template('editar_receta.html', receta=receta)
    else:
        return redirect('/login')

@app.route('/recetas/editar/<int:id>', methods=['POST'])
def editar_recetas(id):
    if 'usuario_id' in session:
        print(session['usuario_id'])
        if request.form['under_30_minutes'] == "Yes":
            under_30_minutes = True
        else:
            under_30_minutes = False
        data = {
            "id": id,
            "name": request.form['name'],
            "description": request.form['description'],
            "instructions": request.form['instructions'],
            "under_30_minutes": under_30_minutes,
            "created_at": request.form['created_at'],
            "user_id": session['usuario_id']
        }
        validar_receta= Recipes.validar_receta(data)
        if validar_receta == False:
            return redirect(f'/editar/receta/{id}')
        else:
            editar_receta= Recipes.editar_una_receta(data)
            print(editar_receta)
            return redirect('/recetas')
    else:
        return redirect('/login')
    
@app.route('/detalle/receta/<int:id>', methods=['GET'])
def desplegar_detalle_recetas(id):
    if 'usuario_id' in session:
        print(session['usuario_id'])
        data = {
            "id": id
        }
        receta= Recipes.obtener_una_receta(data)
        print(receta)
        return render_template('detalle_receta.html', receta=receta)
    else:
        return redirect('/login')
    
@app.route('/eliminar/receta/<int:id>', methods=['GET'])
def eliminar_receta(id):
    if 'usuario_id' in session:
        print(session['usuario_id'])
        data = {
            "id": id
        }
        eliminar_receta= Recipes.eliminar_una_receta(data)
        print(eliminar_receta)
        return redirect('/recetas')
    else:
        return redirect('/login')
