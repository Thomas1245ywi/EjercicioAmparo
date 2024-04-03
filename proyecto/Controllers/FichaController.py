from Models.FichaModel import FichaModel

class FichaController:
    def __init__(self):
        self.ficha_model = FichaModel()



    def set_ficha(self, numero,id_programa):
        self.ficha_model.set_ficha(numero,id_programa)

    def get_fichas(self):
        return self.ficha_model.get_fichas()

    def cerrar_conexion(self):
        self.ficha_model.cerrar_conexion()

    
    