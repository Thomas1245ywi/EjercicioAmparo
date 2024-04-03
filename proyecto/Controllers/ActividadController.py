from Models.ActividadModel import ActividadModel

class ActividadController:
    def __init__(self):
        self.actividad_model = ActividadModel()

    def obtener_nota_actividad(self, id_actividad):
        return self.actividad_model.obtener_nota_actividad(id_actividad)


    def set_actividad(self, nombre, nota, id_resultado):
        self.actividad_model.set_actividad(nombre, nota, id_resultado)

    def get_actividades(self):
        self.actividad_model.get_actividades()

    def cerrar_conexion(self):
        self.actividad_model.cerrar_conexion()

    
    