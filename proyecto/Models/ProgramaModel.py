import sqlite3 as sql


class ProgramaModel:
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Programa (
                id INTEGER PRIMARY KEY,
                nombre TEXT, 
                duracion TEXT
            );
        """)


        self.conn.commit()

    def set_programa(self, nombre, duracion):
        sentencia = 'INSERT INTO Programa(nombre, duracion) VALUES (?,?)'
        self.cursor.execute(sentencia, (nombre, duracion))

    def get_programas(self):
        self.cursor.execute('SELECT numero FROM  Programa ')
        return self.cursor.fetchall()


    def cerrar_conexion(self):
        self.conn.close()







