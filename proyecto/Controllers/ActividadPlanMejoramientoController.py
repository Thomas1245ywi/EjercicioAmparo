from proyecto.Models.ActividadPlanMejoramientoModel import ActividadPlanMejoramientoModel

class ActividadPlanMejoramientoController:
    def __init__(self):
        self.actividad_plan_mejoramiento_model = ActividadPlanMejoramientoModel()


    def get_planes(self):
        return self.actividad_plan_mejoramiento_model.get_planes()



    def asignar_actividad_plan_mejoramiento(self, id_plan, id_actividad):
        self.actividad_plan_mejoramiento_model.asignar_actividad_plan_mejoramiento(id_plan,id_actividad)


    def obtener_actividades_plan_mejoramiento(self, id_plan):
        return self.actividad_plan_mejoramiento_model.obtener_actividades_plan_mejoramiento(id_plan)
    
    def obtener_actividades_plan_mejoramiento_for_table(self, id_plan):
        return self.actividad_plan_mejoramiento_model.obtener_actividades_plan_mejoramiento_for_table(id_plan)

    def cerrar_conexion(self):
        self.actividad_plan_mejoramiento_model.cerrar_conexion()

    
    