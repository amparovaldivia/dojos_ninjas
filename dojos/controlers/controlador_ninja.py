from dojos import app
from flask import render_template,redirect,request,redirect
from dojos import modelo
from dojos.modelo.dojos import Dojos
from dojos.modelo.ninjas import Ninjas

@app.route('/ninja')
def ingresar():
    gimnacios = Dojos.traer_dojos()
    return render_template('ninja.html', dojos=gimnacios) 


@app.route('/ninja',methods=['post'])
def inscripcion():
    print(request.form,'informacion del formulario')
    
    data={
        'dojos_id':request.form['lista_dojo'],
        'nombre':request.form['nombre'],
        'apellido':request.form['apellido'],
        'edad':request.form['edad'],
        'email':request.form['email']
        }
    Ninjas.crear_ninjas(data)
    return redirect(f'/{request.form["lista_dojo"]}') 
    


