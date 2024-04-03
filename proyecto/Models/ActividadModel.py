import sqlite3 as sql


class ActividadModel:
    def __init__(self):
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Actividad (
                id INTEGER PRIMARY KEY,
                nombre TEXT, 
                nota FLOAT,
                id_resultado INTEGER,
                id_estado INTEGER,
                FOREIGN KEY(id_resultado) REFERENCES ResultadoAprendizaje(id),
                FOREIGN KEY(id_estado) REFERENCES Estado(id)
            );
        """)

        self.conn.commit()

    def set_actividad(self, nombre, id_resultado,estado):
  
        sentencia2 = 'SELECT id FROM Estado WHERE nombre = ?' 
        estado_id = self.cursor.execute(sentencia2,(estado,)).fetchone()
        sentencia = f'INSERT INTO Actividad(nombre, id_resultado,id_estado) VALUES (?,?,?)'

        self.cursor.execute(sentencia, (nombre, id_resultado, estado_id))
        self.conn.commit()

    def calificar_actividad(self, id_actividad, nota):
        sentencia = 'UPDATE Actividad SET nota = ? WHERE id = ?'
        self.cursor.execute(sentencia, (nota, id_actividad))
        self.conn.commit()





    def get_actividades(self):
        self.cursor.execute('SELECT * FROM Actividad')
        return self.cursor.fetchall()

    def obtener_nota_actividad(self, id_actividad):
        self.cursor.execute('SELECT nota FROM Actividad WHERE id = ?', (id_actividad,))
        nota = self.cursor.fetchone()
        return nota[0] if nota else None

    def cerrar_conexion(self):
        self.conn.close()