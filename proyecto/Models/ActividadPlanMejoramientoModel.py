
import sqlite3 as sql



class ActividadPlanMejoramientoModel:
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ActividadPlanMejoramiento (
                id INTEGER PRIMARY KEY,
                id_plan INTEGER,
                id_actividad INTEGER,
                FOREIGN KEY(id_plan) REFERENCES PlanMejoramiento(id),
                FOREIGN KEY(id_actividad) REFERENCES Actividad(id)
            );


                                    
            );
                    
        """)



        self.conn.commit()

    def asignar_actividad_plan_mejoramiento(self, id_plan, id_actividad):
        sentencia = 'INSERT INTO ActividadPlanMejoramiento (id_plan, id_actividad) VALUES (?, ?)'
        self.cursor.execute(sentencia, (id_plan, id_actividad))
        self.conn.commit()

    def obtener_actividades_plan_mejoramiento(self, id_plan):
        sentencia = 'SELECT id_actividad FROM ActividadPlanMejoramiento WHERE id_plan = ?'
        self.cursor.execute(sentencia, (id_plan,))
        return self.cursor.fetchall()
    
    def cerrar_conexion(self):
        self.conn.close()