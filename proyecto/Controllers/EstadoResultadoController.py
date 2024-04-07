import sqlite3 as sql
from Models.EstadoResultadoModel import EstadoResultadoModel


class EstadoResultadoController:
    
    def __init__(self):
        self.estado_model = EstadoResultadoModel()



    def set_estado(self, nombre):
        self.estado_model.set_estado(nombre)

    def get_estados(self):
        return self.estado_model.get_estados()
    
    def get_estado_por_nombre(self,estado):
        return self.estado_model.get_estado_por_nombre(estado)

    def cerrar_conexion(self):
        self.estado_model.cerrar_conexion()


