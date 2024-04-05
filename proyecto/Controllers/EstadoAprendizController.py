import sqlite3 as sql
from Models.EstadoAprendizModel import EstadoAprendizModel


class EstadoAprendizController:
    
    def __init__(self):
        self.estado_aprendiz_model = EstadoAprendizModel()



    def set_estado(self, nombre):
        self.estado_aprendiz_model.set_estado(nombre)

    def get_estados(self):
        return self.estado_aprendiz_model.get_estados()

    def cerrar_conexion(self):
        self.estado_aprendiz_model.cerrar_conexion()


