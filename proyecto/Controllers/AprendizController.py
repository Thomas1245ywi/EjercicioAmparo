
from Models.AprendizModel import AprendizModel



class AprendizController:
    def __init__(self):
        self.aprendiz_model = AprendizModel()



    def set_aprendiz(self, nombre, edad, id_ficha,id_resultado,estado_name = "En Formacion"):
        self.aprendiz_model.set_aprendiz(nombre, edad, id_ficha,id_resultado,estado_name)

    def cambiar_estado(self, id_estado, id_aprendiz):
        self.aprendiz_model.cambiar_estado(id_estado,id_aprendiz)

    def get_aprendiz_por_plan(self, id_plan):
    
        return self.aprendiz_model.get_aprendiz_por_plan(id_plan)
    

    

    def get_aprendicez_por_plan(self):
        return self.aprendiz_model.get_aprendicez_por_plan()
         
         

    def get_aprendicez(self):
        return self.aprendiz_model.get_aprendicez()
    
    def get_aprendicez_for_table(self):
        return self.aprendiz_model.get_aprendicez_for_table()   

    def cerrar_conexion(self):
        self.aprendiz_model.cerrar_conexion()

    
    