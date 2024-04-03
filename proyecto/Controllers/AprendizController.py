
from Models.AprendizModel import AprendizModel



class AprendizController:
    def __init__(self):
        self.aprendiz_model = AprendizModel()



    def set_aprendiz(self, nombre, edad, id_ficha,id_resultado):
        self.aprendiz_model.set_aprendiz(nombre, edad, id_ficha,id_resultado)

    def get_aprendicez(self):
        return self.aprendiz_model.get_aprendicez()

    def cerrar_conexion(self):
        self.aprendiz_model.cerrar_conexion()

    
    