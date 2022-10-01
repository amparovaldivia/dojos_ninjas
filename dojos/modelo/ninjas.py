from dojos.configuracion.mysqlconnection import BaseDeDatos
class Ninjas:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.email = data['email']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']
    @classmethod
    def crear_ninjas(cls,data):
        query='INSERT INTO ninjas(nombre,apellido,edad,email,dojos_id) values (%(nombre)s,%(apellido)s,%(edad)s,%(email)s,%(dojos_id)s);'
        resultado=BaseDeDatos('dojos_ninjas').traer_instancia(query,data)
        return resultado
    @classmethod  
    def traer_ninjas(cls):
        query='SELECT * From ninjas;'
        resultado=BaseDeDatos('dojos_ninjas').traer_instancia(query)
        todos_ninjas = []
        for un_ninja in resultado:
            todos_ninjas.append(cls(un_ninja))
        return todos_ninjas

