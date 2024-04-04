import sqlite3 as sql
from Models.EstadoModel import EstadoModel 

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

    def set_actividad(self, nombre, id_resultado, estado):
        # Buscar el ID del estado por su nombre
        estado_id = EstadoModel.obtener_estado_nombre(estado)
        print(estado_id)

        if estado_id:
            # Insertar la actividad en la base de datos
            sentencia_actividad = 'INSERT INTO Actividad(nombre, id_resultado, id_estado) VALUES (?, ?, ?)'
            datos_actividad = (nombre, id_resultado, estado_id[0])  # estado_id es una tupla, tomamos el primer elemento
            self.cursor.execute(sentencia_actividad, datos_actividad)
            self.conn.commit()
            print("Actividad agregada exitosamente.")
        else:
            print(f"No se encontró un estado con el nombre '{estado}'. No se pudo agregar la actividad.")

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
