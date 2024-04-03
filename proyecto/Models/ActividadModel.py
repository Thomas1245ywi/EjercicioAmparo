import sqlite3 as sql


class ActividadModel:
    def _init_(self):
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

    def set_actividad(self, nombre, nota, id_resultado):
        # Calcular el estado del estudiante
        estado = 'Aprobado' if nota and nota >= 70 else 'Por Evaluar'

        # Insertar el estado en la tabla Estado
        self.cursor.execute("INSERT INTO Estado(nombre) VALUES (?)", (estado,))
        self.conn.commit()

        # Obtener el ID del estado insertado
        id_estado = self.cursor.lastrowid

        # Insertar la actividad en la tabla Actividad
        sentencia = 'INSERT INTO Actividad(nombre, nota, id_resultado, id_estado) VALUES (?,?,?,?)'
        self.cursor.execute(sentencia, (nombre, nota, id_resultado, id_estado))
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