from dojos import app
from flask import render_template,request,redirect
from dojos import modelo
from dojos.modelo.dojos import Dojos
@app.route('/<int:dojo_id>')
def mostrar_dojo(dojo_id):
    dojo=Dojos.devolver_todo(dojo_id)
    return render_template('dojo1.html',nombre_dojo=dojo.nombres,ninjas=dojo.ninjas)
