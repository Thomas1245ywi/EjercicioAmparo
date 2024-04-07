import sqlite3 as sql
from .EstadoResultadoModel import EstadoResultadoModel
from .ResultadoModel import ResultadoModel

class PlanMejoramientoModel:
    
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()
        self.estado_resultado_model = EstadoResultadoModel()
        self.resultado_model = ResultadoModel()
        self.contador = 0

        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS PlanMejoramiento(
                id INTEGER PRIMARY KEY,
                nombre VARCHAR(100),
                fecha_asignacion DATE,
                fecha_hora_entrega DATETIME,
                descripcion Varchar(255),
                evaluacion FLOAT,
                retroalimetacion VARCHAR(255),
     
                
                id_resultado INTEGER,
                FOREIGN KEY (id_resultado) REFERENCES Resultado(id)
            );
        """)


        self.conn.commit()

    def set_plan_mejoramiento(self,nombre,fecha_asignacion,fecha_hora_entrega,descripcion,id_resultado):
        sentencia = "INSERT INTO PlanMejoramiento(nombre,fecha_asignacion,fecha_hora_entrega,descripcion,id_resultado) VALUES (?,?,?,?,?)"
        self.cursor.execute(sentencia, (nombre,fecha_asignacion,fecha_hora_entrega,descripcion,id_resultado))

        self.conn.commit()

    def get_plan_mejoramientos(self):
        # Ejecutar la consulta SQL
        self.cursor.execute("SELECT * FROM PlanMejoramiento")

        # Recuperar los resultados después de ejecutar la consulta
        return self.cursor.fetchall()
    
    def get_plan_mejoramiento(self,id_plan):
        # Ejecutar la consulta SQL
        self.cursor.execute("SELECT retroalimetacion FROM PlanMejoramiento WHERE id = ?",(id_plan,))


        # Recuperar los resultados después de ejecutar la consulta
        return self.cursor.fetchone()
    
    def calificar_plan(self,nota,id_plan):


        if int(nota) >= 70:
            estado = 'Aprobado'

        else:
            estado = 'Plan De Mejoramiento'
            self.contador += 1

        estado_id = self.estado_resultado_model.get_estado_por_nombre(estado)
        print(estado_id)
        resultado = self.cursor.execute("SELECT id_resultado FROM PlanMejoramiento WHERE id = ?",(id_plan,))
        resultado_id = resultado.fetchone()

        self.resultado_model.cambiar_estado(resultado_id,estado_id)

        self.cursor.execute("UPDATE PlanMejoramiento SET evaluacion = ? WHERE id = ?", (nota, id_plan))
        self.conn.commit()

        if estado == 'Plan De Mejoramiento':
            
            return id_plan,resultado_id, self.contador







    
    def agregar_retroalimentacion(self,retroalimentacion, fecha_nueva,id_plan):
        self.cursor.execute("UPDATE PlanMejoramiento SET retroalimetacion = ?, fecha_hora_entrega = ? WHERE id = ?",(retroalimentacion,fecha_nueva,id_plan))
        self.conn.commit()
 
         

    def cerrar_conexion(self):
        self.conn.close()





