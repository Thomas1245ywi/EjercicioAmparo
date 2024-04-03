import sqlite3 as sql
from Models.EstadoModel import EstadoModel


class EstadoController:
    
    def __init__(self):
        self.estado_model = EstadoModel()



    def set_estado(self, nombre):
        self.estado_model.set_estado(nombre)

    def get_estados(self):
        return self.estado_model.get_estados()

    def cerrar_conexion(self):
        self.estado_model.cerrar_conexion()


