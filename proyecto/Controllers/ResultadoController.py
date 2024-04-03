from Models.ResultadoModel import ResultadoModel

class ResultadoController:
    def __init__(self):
        self.resultado_model = ResultadoModel()



    def set_resultado(self, nombre,id_competencia):
        self.resultado_model.set_resultado(nombre,id_competencia)

    def get_resultados(self):
        return self.resultado_model.get_resultados()

    def cerrar_conexion(self):
        self.resultado_model.cerrar_conexion()

    
    