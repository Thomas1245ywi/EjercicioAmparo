import sqlite3 as sql



class ResultadoModel:
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Resultado (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                id_competencia INTEGER,
                FOREIGN KEY(id_competencia) REFERENCES Competencia(id)
                                                      
            );
                    
        """)



        self.conn.commit()

    def set_resultado(self, nombre,id_competencia):
        sentencia = 'INSERT INTO Resultado(nombre,id_competencia) VALUES (?,?)'
        self.cursor.execute(sentencia, (nombre,id_competencia))
        self.conn.commit()

    def get_resultados(self):
        self.cursor.execute('SELECT  * FROM Resultado')
        return self.cursor.fetchall()


    def cerrar_conexion(self):
        self.conn.close()
