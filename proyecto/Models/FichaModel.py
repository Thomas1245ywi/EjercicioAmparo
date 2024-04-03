import sqlite3 as sql


class FichaModel:
    
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Ficha(
                id INTEGER PRIMARY KEY,
                numero TEXT, 
                id_programa INTEGER,
                FOREIGN KEY(id_programa) REFERENCES Programa(id)

            );
        """)


        self.conn.commit()

    def set_ficha(self,numero,id_programa):
        sentencia = "INSERT INTO Ficha(numero,id_programa) VALUES (?,?)"
        self.cursor.execute(sentencia, (numero,id_programa))

    def get_fichas(self):
        # Ejecutar la consulta SQL
        self.cursor.execute("SELECT * FROM Ficha")

        # Recuperar los resultados después de ejecutar la consulta
        cursos = self.cursor.fetchall()

        return cursos

    def cerrar_conexion(self):
        self.conn.close()





