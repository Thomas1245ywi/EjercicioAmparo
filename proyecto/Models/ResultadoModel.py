import sqlite3 as sql



class ResultadoModel:
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Resultado (
                id INTEGER PRIMARY KEY,
                nombre TEXT                              
            );
                    
        """)



        self.conn.commit()

    def set_resultado(self, nombre):
        sentencia = 'INSERT INTO Resultado(nombre) VALUES (?)'
        self.cursor.execute(sentencia, (nombre,))
        self.conn.commit()

    def get_resultados(self):
        self.cursor.execute('SELECT  * FROM Resultado')
        return self.cursor.fetchall()


    def cerrar_conexion(self):
        self.conn.close()
