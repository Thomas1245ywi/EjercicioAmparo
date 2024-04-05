
from Models.AprendizModel import AprendizModel



class AprendizController:
    def __init__(self):
        self.aprendiz_model = AprendizModel()



    def set_aprendiz(self, nombre, edad, id_ficha,id_resultado,estado_name = "En Formacion"):
        self.aprendiz_model.set_aprendiz(nombre, edad, id_ficha,id_resultado,estado_name)

    def get_aprendicez(self):
        return self.aprendiz_model.get_aprendicez()
    
    def get_aprendicez_for_table(self):
        return self.aprendiz_model.get_aprendicez_for_table()   

    def cerrar_conexion(self):
        self.aprendiz_model.cerrar_conexion()

    
    