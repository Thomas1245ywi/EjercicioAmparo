from Models.ProgramaModel import ProgramaModel

class ProgramaController:
    def __init__(self):
        self.programa_model = ProgramaModel()



    def set_programa(self, numero,id_programa):
        self.programa_model.set_programa(numero,id_programa)

    def get_programas(self):
        self.programa_model.get_programas()

    def cerrar_conexion(self):
        self.programa_model.cerrar_conexion()

    
    