import sqlite3 as sql
from Models.PlanMejoramientoModel import PlanMejoramientoModel


class PlanMejoramientoController:
    
    def __init__(self):
        self.plan_mejoramiento_model = PlanMejoramientoModel()



    def set_plan(self, nombre,id_resultado):
        self.plan_mejoramiento_model.set_plan_mejoramiento(nombre,id_resultado)

    def get_planes(self):
        return self.plan_mejoramiento_model.get_plan_mejoramientos()

    def cerrar_conexion(self):
        self.plan_mejoramiento_model.cerrar_conexion()


