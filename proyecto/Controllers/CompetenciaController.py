from Models.CompetenciaModel import CompetenciaModel

class AprendizController:
    def __init__(self):
        self.competencia_model = CompetenciaModel()



    def set_competencia(self, nombre):
        self.competencia_model.set_competencia(nombre)

    def get_competencias(self):
        self.competencia_model.get_competencias()

    def cerrar_conexion(self):
        self.competencia_model.cerrar_conexion()

    
    