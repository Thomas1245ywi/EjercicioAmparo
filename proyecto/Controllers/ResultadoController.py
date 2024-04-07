from Models.ResultadoModel import ResultadoModel

class ResultadoController:
    def __init__(self):
        self.resultado_model = ResultadoModel()



    def set_resultado(self, nombre,id_competencia,estado_name = "Por Evaluar"):
        self.resultado_model.set_resultado(nombre,id_competencia,estado_name)

    def get_resultados(self):
        return self.resultado_model.get_resultados()
    
    def get_resultados_for_table(self):
        return self.resultado_model.get_resultados_for_table()

    def cerrar_conexion(self):
        self.resultado_model.cerrar_conexion()

    def cambiar_estado(self,id_resultado, id_estado):
        self.resultado_model.cambiar_estado(id_resultado, id_estado)

    
    