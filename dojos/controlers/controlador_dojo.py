from dojos import app
from flask import render_template,request,redirect
from dojos import modelo
from dojos.modelo.dojos import Dojos


@app.route('/')
def agregar_dojo():
    dojos=Dojos.traer_dojos()
    return render_template('dojo.html',dojos=dojos)

@app.route('/', methods=['POST'])
def crear_dojo():
    print(request.form)
    data={
        "nombres":request.form['dojo']
    }
    Dojos.crear_dojo(data)
    return redirect('/')


