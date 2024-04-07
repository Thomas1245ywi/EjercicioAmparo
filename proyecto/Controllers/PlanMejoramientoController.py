import sqlite3 as sql
from Models.PlanMejoramientoModel import PlanMejoramientoModel


class PlanMejoramientoController:
    
    def __init__(self):
        self.plan_mejoramiento_model = PlanMejoramientoModel()


    def calificar_plan(self,nota,id_resultado):
        # Ejecutar la consulta SQL
        return self.plan_mejoramiento_model.calificar_plan(nota,id_resultado)

    def set_plan(self, nombre,fecha_asignacion,fecha_hora_entrega,descripcion,id_resultado):
        self.plan_mejoramiento_model.set_plan_mejoramiento(nombre,fecha_asignacion,fecha_hora_entrega,descripcion,id_resultado)

    def get_planes(self):
        return self.plan_mejoramiento_model.get_plan_mejoramientos()
    
    def get_plan_mejoramiento(self,id_plan):
        # Ejecutar la consulta SQL
        return self.plan_mejoramiento_model.get_plan_mejoramiento(id_plan)
        
    
    def agregar_retroalimentacion(self,retroalimentacion, fecha_nueva,id_plan):
        self.plan_mejoramiento_model.agregar_retroalimentacion(retroalimentacion,fecha_nueva,id_plan)



    def cerrar_conexion(self):
        self.plan_mejoramiento_model.cerrar_conexion()


