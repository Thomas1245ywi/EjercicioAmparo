from Models.ResultadoModel import ResultadoModel

class ResultadoController:
    def __init__(self):
        self.resultado_model = ResultadoModel()



    def set_resultado(self, nombre):
        self.resultado_model.set_resultado(nombre)

    def get_resultados(self):
        return self.resultado_model.get_resultados()

    def cerrar_conexion(self):
        self.resultado_model.cerrar_conexion()

    
    