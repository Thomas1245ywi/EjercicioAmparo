from Models.ActividadModel import ActividadModel

class ActividadController:
    def __init__(self):
        self.actividad_model = ActividadModel()

    def obtener_nota_actividad(self, id_actividad):
        return self.actividad_model.obtener_nota_actividad(id_actividad)


    def set_actividad(self, nombre, id_resultado,estado = "Por Evaluar"):
        self.actividad_model.set_actividad(nombre, id_resultado,estado)

    def calificar_actividad(self, id_actividad, nota):
        self.actividad_model.calificar_actividad(id_actividad, nota)

    def get_actividades(self):
        return self.actividad_model.get_actividades()

    def cerrar_conexion(self):
        self.actividad_model.cerrar_conexion()

    
    