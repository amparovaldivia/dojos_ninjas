from dojos.configuracion.mysqlconnection import BaseDeDatos
from dojos.modelo.ninjas import Ninjas

class Dojos:
    def __init__(self,data):
        self.id = data['id']
        self.nombres = data['nombres']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']
        self.ninjas=[]
        
    @classmethod
    def crear_dojo(cls,data):
        query='INSERT INTO dojos(nombres) values (%(nombres)s);'
        resultado= BaseDeDatos('dojos_ninjas').traer_instancia(query,data)
        return resultado

    @classmethod
    def traer_dojos(cls):
        query='SELECT * FROM dojos;'
        resultado= BaseDeDatos('dojos_ninjas').traer_instancia(query)
        todos_dojos = []
        for un_dojo in resultado:
            todos_dojos.append(cls(un_dojo))
        return todos_dojos
        
    @classmethod
    def devolver_todo(cls,id):
        query='SELECT * FROM dojos WHERE id=%(id)s;'
        resultado= BaseDeDatos('dojos_ninjas').traer_instancia(query,{'id':id})
        todos_dojos = cls(resultado[0])
        query2='SELECT * FROM ninjas WHERE dojos_id=%(id)s;'
        resultado2= BaseDeDatos('dojos_ninjas').traer_instancia(query2,{'id':id})
        todos_ninjas = []
        for un_ninja in resultado2:
            todos_ninjas.append(Ninjas(un_ninja))
        todos_dojos.ninjas=todos_ninjas    
        return todos_dojos
        

