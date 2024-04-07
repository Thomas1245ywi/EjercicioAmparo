import sqlite3 as sql


class ResultadoActividadModel:
    def __init__(self):
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ResultadoActividad (
                id_resultado INTEGER,
                id_actividad INTEGER,
                PRIMARY KEY (id_resultado, id_actividad),
                FOREIGN KEY (id_resultado) REFERENCES Resultado(id),
                FOREIGN KEY (id_actividad) REFERENCES Actividad(id)
            );
        """)
        self.conn.commit()

    def agregar_relacion_resultado_actividad(self, id_resultado, id_actividad):
        self.cursor.execute("INSERT INTO ResultadoActividad (id_resultado, id_actividad) VALUES (?, ?)",
                            (id_resultado, id_actividad))
        self.conn.commit()

    def obtener_actividades_por_resultado(self, id_resultado):
        self.cursor.execute("""SELECT 
        ResultadoActividad.id_actividad, 
        Actividad.nombre, 
        Actividad.nota, 
        Estado.nombre 
        FROM 
            ResultadoActividad 
        INNER JOIN 
            Actividad ON Actividad.id = ResultadoActividad.id_actividad 
        INNER JOIN 
            Estado ON Actividad.id_estado = Estado.id
        WHERE 
            id_resultado = ?;""", (id_resultado,))
        return self.cursor.fetchall()
    

   
    
    


    def obtener_resultado_por_actividad(self, id_actividad):


        self.cursor.execute("""SELECT 
        ResultadoActividad.id_resultado, 
        Resultado.nombre
        FROM 
            ResultadoActividad 
        INNER JOIN 
            Resultado ON Resultado.id = ResultadoActividad.id_resultado 
        
        WHERE 
            id_actividad = ?;""", (id_actividad,))
        return self.cursor.fetchone()
        
    
    def cerrar_conexion(self):
        self.conn.close()
