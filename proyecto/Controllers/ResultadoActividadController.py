from proyecto.Models.ResultadoActividadModel import ResultadoActividadModel

class ResultadoActividadController:
    def __init__(self):
        self.resultado_actividad_model = ResultadoActividadModel()



    def agregar_relacion_resultado_actividad(self, id_resultado, id_actividad):
        self.resultado_actividad_model.agregar_relacion_resultado_actividad(id_resultado, id_actividad)


    def obtener_actividades_por_resultado(self, id_resultado):
        return self.resultado_actividad_model.obtener_actividades_por_resultado(id_resultado)
    
    def obtener_resultado_por_actividad(self, id_actividad):
        return self.resultado_actividad_model.obtener_resultado_por_actividad(id_actividad)

    def cerrar_conexion(self):
        self.resultado_actividad_model.cerrar_conexion()

    
    