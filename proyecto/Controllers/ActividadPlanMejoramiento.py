from proyecto.Models.ActividadPlanMejoramientoModel import ActividadPlanMejoramientoModel

class ActividadController:
    def __init__(self):
        self.actividad_plan_mejoramiento_model = ActividadPlanMejoramientoModel()



    def asignar_actividad_plan_mejoramiento(self, id_plan, id_actividad):
        self.actividad_plan_mejoramiento_model.asignar_actividad_plan_mejoramiento(id_plan,id_actividad)


    def obtener_actividades_plan_mejoramiento(self, id_plan):
        return self.actividad_plan_mejoramiento_model.obtener_actividades_plan_mejoramiento(id_plan)

    def cerrar_conexion(self):
        self.actividad_plan_mejoramiento_model.cerrar_conexion()

    
    