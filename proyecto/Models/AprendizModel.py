import sqlite3 as sql



class AprendizModel:
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Aprendiz (
                id INTEGER PRIMARY KEY,
                nombre TEXT, 
                edad INTEGER,
                id_ficha INTEGER,
                id_estado INTEGER,
                id_resultado INTEGER,
                FOREIGN KEY (id_resultado) REFERENCES Resultado(id)
                FOREIGN KEY(id_ficha) REFERENCES Ficha(id),
                FOREIGN KEY(id_estado) REFERENCES Estado(id)


                                    
            );
                    
        """)



        self.conn.commit()

    def set_aprendiz(self, nombre, edad, id_ficha, id_resultado):
        sentencia = 'INSERT INTO Aprendiz(nombre, edad, id_ficha,id_resultado) VALUES (?,?,?,?)'
        self.cursor.execute(sentencia, (nombre, edad, id_ficha,id_resultado))
        self.conn.commit()

    def get_aprendicez(self):
        self.cursor.execute('SELECT * FROM  Aprendiz')
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()









