import pymysql.cursors
# esta clase nos dará una instancia de una conexión a nuestra base de datos
class BaseDeDatos:
    def __init__(self, db):
        # cambiar el usuario y la contraseña según sea necesario
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        
        self.connection = connection
    
    def traer_instancia(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    
                    result = cursor.fetchall()
                    return result
                else:
                    
                    self.connection.commit()
            except Exception as e:
                
                print("Something went wrong", e)
                return False
            finally:
            
                self.connection.close() 
# connectToMySQL recibe la base de datos que estamos usando y la usa para crear una instancia de MySQLConnection
def connectarAMySQL(db):
    return BaseDeDatos(db)