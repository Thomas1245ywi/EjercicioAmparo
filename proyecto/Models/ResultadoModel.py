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
                id_estado INTEGER,
                
                FOREIGN KEY(id_competencia) REFERENCES Competencia(id),
                FOREIGN KEY(id_estado) REFERENCES EstadoResultado(id)

                                                      
            );
                    
        """)



        self.conn.commit()

    def set_resultado(self, nombre,id_competencia,estado_name):

        sentencia_estado = 'SELECT id FROM EstadoResultado WHERE nombre = ?'
        estado = self.conn.execute(sentencia_estado,(estado_name,)).fetchone()
        estado_id = estado[0]





        sentencia = 'INSERT INTO Resultado(nombre,id_competencia,id_estado) VALUES (?,?,?)'
        self.cursor.execute(sentencia, (nombre,id_competencia,estado_id))
        self.conn.commit()





    def get_resultados(self):
        self.cursor.execute('SELECT  * FROM Resultado')
        return self.cursor.fetchall()
    
    def get_resultados_for_table(self):
        self.cursor.execute('SELECT  Resultado.nombre, Competencia.nombre FROM Resultado INNER JOIN Competencia ON id_competencia = Competencia.id')
        return self.cursor.fetchall()


    def cerrar_conexion(self):
        self.conn.close()
