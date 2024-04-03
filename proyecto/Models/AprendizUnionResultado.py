import sqlite3 as sql



class AprendizUnionResultadoModel:
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS AprendizUnionResultado (
                id INTEGER PRIMARY KEY,
                idAprendiz INTEGER,
                idResultado INTEGER,

                FOREIGN KEY(idAprendiz) REFERENCES Aprendiz(id),
                FOREIGN KEY(idResultado) REFERENCES Resultado(id)


                                    
            );
                    
        """)



        self.conn.commit()

    def set_aprendiz(self, nombre, edad, id_ficha, id_estado):
        sentencia = 'INSERT INTO Aprendiz(nombre, edad, id_ficha,id_estado) VALUES (?,?,?,?)'
        self.cursor.execute(sentencia, (nombre, edad, id_ficha,id_estado))
        self.conn.commit()

    def get_aprendicez(self):
        self.cursor.execute('SELECT * FROM  Aprendiz')
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()









