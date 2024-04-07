import sqlite3 as sql
from Models.EstadoModel import EstadoModel 
from Models.PlanMejoramientoModel import PlanMejoramientoModel
from Models.ResultadoActividadModel import ResultadoActividadModel




class ActividadModel:
    def __init__(self):
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()
        self.plan_mejoramiento_model = PlanMejoramientoModel()
        self.resultado_actividad_model = ResultadoActividadModel()
        self.cantidad = 0

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Actividad (
                id INTEGER PRIMARY KEY,
                nombre TEXT, 
                nota FLOAT,
                id_estado INTEGER,
                FOREIGN KEY(id_estado) REFERENCES Estado(id)
            );
        """)

        self.conn.commit()

    def set_actividad(self, nombre, estado):
        # Buscar el ID del estado por su nombre
        sentencia_estado = 'SELECT id FROM Estado WHERE nombre = ?'
        estado_id = self.conn.execute(sentencia_estado,(estado,)).fetchone()
        estado = estado_id[0]
        print(estado)

        if estado:
            # Insertar la actividad en la base de datos
            sentencia_actividad = 'INSERT INTO Actividad(nombre,  id_estado) VALUES (?, ?)'
            self.cursor.execute(sentencia_actividad, (nombre,estado))
            self.conn.commit()
            print("Actividad agregada exitosamente.")
        else:
            print(f"No se encontró un estado con el nombre '{estado}'. No se pudo agregar la actividad.")

    def calificar_actividad(self, id_actividad, nota):

        if int(nota) >= 70:
            estado = 'Aprobado'

        else:
            estado = 'Desaprobado'
        

        actividades_arreglo = []
        sentencia_estado = 'SELECT id FROM Estado WHERE nombre = ?'
        estado_id = self.conn.execute(sentencia_estado,(estado,)).fetchone()
        estado = estado_id[0]
        sentencia = 'UPDATE Actividad SET nota = ?,id_estado = ?  WHERE id = ?'
        self.cursor.execute(sentencia, (nota, estado, id_actividad))
        self.conn.commit()
        actividadesCalificadas = []


        resultado = self.resultado_actividad_model.obtener_resultado_por_actividad(id_actividad)
        actividades = self.resultado_actividad_model.obtener_actividades_por_resultado(resultado[0])

    

        
        cantidad_actividades = len(actividades)
        if cantidad_actividades == 3:
            actividades_con_nota = [actividad for actividad in actividades if actividad[2] is not None]
            if len(actividades_con_nota) == 3:
                # Todas las actividades tienen nota, procede con el proceso
                for actividad in actividades_con_nota:
                    actividadesCalificadas.append(True)
                    self.cantidad += 1

                for actividad in actividades:
                    if actividad[3] == "Desaprobado":
                            
                        actividades_arreglo.append(actividad)

                return actividades_arreglo
            else:
               
                print("No todas las actividades tienen nota")

             
        

            
       
                
            
        
        
            
        


    def get_actividades(self):
        self.cursor.execute('SELECT * FROM Actividad')
        return self.cursor.fetchall()
    
    def obtener_actividad_por_id(self, id_actividad):
        self.cursor.execute('SELECT * FROM Actividad WHERE id = ?',(id_actividad,))

    def obtener_nota_actividad(self, id_actividad):
        self.cursor.execute('SELECT nota FROM Actividad WHERE id = ?', (id_actividad,))
        nota = self.cursor.fetchone()
        return nota[0] if nota else None

    def cerrar_conexion(self):
        self.conn.close()
