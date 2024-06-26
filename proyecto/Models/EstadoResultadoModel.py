import sqlite3 as sql


class EstadoResultadoModel:
    
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS EstadoResultado(
                id INTEGER PRIMARY KEY,
                nombre VARCHAR(100)
            );
        """)


        self.conn.commit()

    def set_estado(self,nombre):
        sentencia = "INSERT INTO EstadoResultado(nombre) VALUES (?)"
        self.cursor.execute(sentencia, (nombre))

    def get_estados(self):
        # Ejecutar la consulta SQL
        self.cursor.execute("SELECT * FROM EstadoResultado")

        # Recuperar los resultados después de ejecutar la consulta
        return self.cursor.fetchall()
    

    def get_estado_por_nombre(self,estado):
        # Ejecutar la consulta SQL
        self.cursor.execute("SELECT id FROM EstadoResultado WHERE nombre = ?",(estado,))

        # Recuperar los resultados después de ejecutar la consulta
        return self.cursor.fetchone()
    

 
         

    def cerrar_conexion(self):
        self.conn.close()





