import sqlite3 as sql



class CompetenciaModel:
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Competencia (
                id INTEGER PRIMARY KEY,
                nombre TEXT, 
                id_programa INTEGER,
                FOREIGN KEY(id_programa) REFERENCES Programa(id)
                                             
            );
                    
        """)



        self.conn.commit()

    def set_competencia(self, nombre):
        sentencia = 'INSERT INTO Competencia(nombre) VALUES (?)'
        self.cursor.execute(sentencia, (nombre))

    def get_competencias(self):
        self.cursor.execute('SELECT * FROM  Competencia  ')
        return self.cursor.fetchall()


    def cerrar_conexion(self):
        self.conn.close()
