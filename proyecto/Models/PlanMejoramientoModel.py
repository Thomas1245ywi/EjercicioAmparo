import sqlite3 as sql


class PlanMejoramientoModel:
    
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS PlanMejoramiento(
                id INTEGER PRIMARY KEY,
                nombre VARCHAR(100),
                id_resultado INTEGER,
                FOREIGN KEY (id_resultado) REFERENCES Resultado(id)
            );
        """)


        self.conn.commit()

    def set_plan_mejoramiento(self,nombre,id_resultado):
        sentencia = "INSERT INTO PlanMejoramiento(nombre,id_resultado) VALUES (?,?)"
        self.cursor.execute(sentencia, (nombre,id_resultado))

        self.conn.commit()

    def get_plan_mejoramientos(self):
        # Ejecutar la consulta SQL
        self.cursor.execute("SELECT * FROM PlanMejoramiento")

        # Recuperar los resultados después de ejecutar la consulta
        return self.cursor.fetchall()
    

 
         

    def cerrar_conexion(self):
        self.conn.close()





