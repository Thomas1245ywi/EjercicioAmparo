import tkinter as tk
from Controllers.FichaController import FichaController
from Controllers.ProgramaController import ProgramaController
from Controllers.AprendizController import AprendizController
from Controllers.ResultadoController import ResultadoController
from Controllers.CompetenciaController import CompetenciaController
from Controllers.EstadoController import EstadoController
from Controllers.EstadoAprendizController import EstadoAprendizController
from Controllers.EstadoResultadoController import EstadoResultadoController

from tkcalendar import DateEntry
from Controllers.ActividadController import ActividadController
from Controllers.ResultadoActividadController import ResultadoActividadController

from Controllers.EstadoController import EstadoController
from Controllers.PlanMejoramientoController import PlanMejoramientoController


import datetime







from tkinter import ttk
ficha_controller = FichaController()
programa_controller = ProgramaController()
aprendiz_controller = AprendizController()
resultado_controller = ResultadoController()
competencia_controller = CompetenciaController()
estado_controller = EstadoController() 
actividad_controller = ActividadController() 
estado_aprendiz_controller = EstadoAprendizController() 
resultado_actividad_controller = ResultadoActividadController()
plan_mejoramiento_controller = PlanMejoramientoController()
estado_resultado_controller = EstadoResultadoController()
actividades_arreglo = []
fecha_seleccionada = None
resultado_final = None
id_plan = None
retroalimentacioncita =  None
contador = None
from tkinter import messagebox


def limpiar_campos():
    entNombre.delete(0, tk.END)
    entEdad.delete(0, tk.END)
    entResultado.delete(0, tk.END)
    entNota.delete(0, tk.END)
    entPlan.delete(0, tk.END)
    entDescipcion.delete(0, tk.END)
    entRetroalimetacion.delete(0, tk.END)

def mostrar_mensaje():
    messagebox.showinfo("Accion Exitosa", "Accion Realizada con exito")
    limpiar_campos()

def cambio_plan_mejoramiento(event):
    global retroalimentacioncita,contador
    
    if contador == 2:
        ocultar_todo()
        lblAviso.grid()

def agregar_retroalimentacion_bd():
    plan_mejoramiento_controller.agregar_retroalimentacion(retroalimentacion.get(),fecha_seleccionada,id_plan)
    print("oki")
    mostrar_mensaje()

def calificar_plan_bd():
    modificar_cmb_Planes()
    global id_plan,contador
    id_plan,id_resultado,contador = plan_mejoramiento_controller.calificar_plan(nota.get(),diccionarioPlanesMejoramiento[opcion_seleccionada_plan.get()])
    if id_plan != None:
        ocultar_todo()
        global retroalimentacioncita
        retroalimentacioncita = plan_mejoramiento_controller.get_plan_mejoramiento(id_plan)


        if retroalimentacioncita[0] is None:

            lblRetroalimentacion.grid()
            entRetroalimetacion.grid()
            lblFechaEntrega.grid()
            datEntrega.grid()
            btnRetroalimentacion.grid()

        else:
            estado = "Desaprobado"
            estado_id = estado_resultado_controller.get_estado_por_nombre(estado)
            resultado_controller.cambiar_estado(id_resultado,estado_id)
            estado_aprendiz = "En Proceso De Desercion"
            aprendiz_id = aprendiz_controller.get_aprendiz_por_plan(id_plan)
            print(aprendiz_id,"holi")

            estado_aprendiz_id = estado_aprendiz_controller.get_estado_por_nombre(estado_aprendiz)

            aprendiz_controller.cambiar_estado(estado_aprendiz_id,aprendiz_id)
            contador = 2
            




            

            ocultar_todo()
            lblAviso.grid()




        





def actualizar_fecha(event):
    global fecha_seleccionada
    fecha_seleccionada = datEntrega.get_date()
    print(fecha_seleccionada)

def modificar_cmb_Resultados():
    global resultados 
    resultados = resultado_controller.get_resultados()

    cmbResultado.config(values= [resultado[1] for resultado in resultados])
    global diccionarioResultados 
    diccionarioResultados = {resultado[1]: resultado[0] for resultado in  resultados}

def modificar_cmb_Actividades():
    global actividades 
    actividades = actividad_controller.get_actividades()

    cmbActividades.config(values= [actividad[1] for actividad in actividades])
    global diccionarioActividades 
    diccionarioActividades = {actividad[1]: actividad[0] for actividad in  actividades}



def modificar_cmb_Fichas():
    global fichas 
    fichas = ficha_controller.get_fichas()

    cmbFicha.config(values= [ficha[1] for ficha in fichas])
    global diccionarioFichas 
    diccionarioFichas = {ficha[1]: ficha[0] for ficha in  fichas}


def modificar_cmb_Planes():
    global planes_mejoramiento,diccionarioPlanesMejoramiento
    
    planes_mejoramiento = plan_mejoramiento_controller.get_planes()

    CmbPlanMejoramiento.config(values= [plan_mejoramiento[1] for plan_mejoramiento in planes_mejoramiento])
    diccionarioPlanesMejoramiento = {plan_mejoramiento[1]: plan_mejoramiento[0] for plan_mejoramiento in  planes_mejoramiento}




def modificar_cmb_estdiantes():
    global a 
    fichas = ficha_controller.get_fichas()

    cmbFicha.config(values= [ficha[1] for ficha in fichas])
    global diccionarioFichas 
    diccionarioFichas = {ficha[1]: ficha[0] for ficha in  fichas}


def modificar_cmb_Competencias():
    competencias = competencia_controller.get_competencias()

    cmbCompetencias.config(values= [competencia[1] for competencia in competencias])
    global diccionarioCompetencias 
    diccionarioCompetencias = {competencia[1]: competencia[0] for competencia in  competencias}



def agregar_aprendiz_bd():

    aprendiz_controller.set_aprendiz(nombre.get(),edad.get(), diccionarioFichas[opcion_seleccionada.get()], diccionarioResultados[opcion_seleccionada_resultado.get()])
    mostrar_mensaje()

def ocultar_todo():
   
    for widget in root.winfo_children():
        widget.grid_forget()

def calificar_actividad_bd():
    modificar_cmb_Actividades()
    global actividades_arreglo, resultado_final
    actividades_arreglo = actividad_controller.calificar_actividad(diccionarioActividades[opcion_seleccionada_actividad.get()],nota.get())
    mostrar_mensaje()
    if actividades_arreglo != None:
        ocultar_todo()
        resultado = []
        
        for actividad_arreglo in actividades_arreglo:

            resultado.append(resultado_actividad_controller.obtener_resultado_por_actividad(actividad_arreglo[0]))
            
        resultado_semifinal = set(resultado)
        resultado_final = resultado_semifinal.pop()


        lblPlanMejoramiento.grid(row=0, column=0, padx=10, pady=10)
        entPlan.grid(row=0, column=1, padx=10, pady=10)
        lblFechaEntrega.grid(row=1, column=0, padx=10, pady=10)
        datEntrega.grid(row=1, column=1, padx=10, pady=10)
        lblDescripcion.grid(row=2, column=0, padx=10, pady=10)
        entDescipcion.grid(row=2, column=1, padx=10, pady=10)
        datEntrega.bind("<<DateEntrySelected>>", actualizar_fecha)

        btnAgregarPlanMejoramiento.grid(row=3, column=0, columnspan=2, padx=10, pady=10) 

    else:
        ocultar_todo()
        lblMensajeExito.grid()








        

def agregar_actividad_bd():
    actividad_controller.set_actividad(nombre.get())
    modificar_cmb_Actividades()
    resultado_actividad_controller.agregar_relacion_resultado_actividad(diccionarioResultados[opcion_seleccionada_resultado.get()],    diccionarioActividades[nombre.get()])
    mostrar_mensaje()
    
def agregar_actividad():
    modificar_cmb_Resultados()

    ocultar_todo()
    lblNombre.grid()
    entNombre.grid()
    lblResultado.grid()
    cmbResultado.grid()
    btnAgregarActividad.grid()

def consultar_actividades():
    pass
                      
def agregar_plan_bd():
    fecha_hoy = datetime.date.today()
    
   

    print(resultado_final)
    plan_mejoramiento_controller.set_plan(plan.get(),fecha_hoy,fecha_seleccionada,descripcion.get(),resultado_final[0])
    mostrar_mensaje()

    
    
    
def calificar_plan():

    ocultar_todo()
    modificar_cmb_Planes()

    lblPlanMejoramiento.grid()
    CmbPlanMejoramiento.grid()

    lblNota.grid()
    entNota.grid()
    btnCalificarPlan.grid()

    

    # Crear una tabla con encabezados
    



def calificar_actividad():
    modificar_cmb_Actividades()
    ocultar_todo()
    lblActividad.grid()
    cmbActividades.grid()
    lblNota.grid()
    entNota.grid()
    btnCalificar.grid()

def agregar_aprendiz():
    modificar_cmb_Resultados()
    ocultar_todo()
    lblNombre.grid()
    entNombre.grid()
    lblEdad.grid()
    entEdad.grid()
    lblFicha.grid()
    cmbFicha.grid()
    lblResultado.grid()
    cmbResultado.grid()
    btnAgregar.grid()



def consultar_estudiantes():
    ocultar_todo()

    aprendicez = aprendiz_controller.get_aprendicez_for_table()

    # Crear una tabla con encabezados
    encabezados = ['Nombre', 'Edad', 'Ficha','Estado','Resultado']
    for i, encabezado in enumerate(encabezados):
        label = tk.Label(root, text=encabezado)
        label.grid(row=0, column=i)

    # Mostrar los datos de los estudiantes en la tabla
    for i, aprendiz in enumerate(aprendicez, start=1):
        nombre = aprendiz[1]
        edad = aprendiz[2]
        ficha = aprendiz[3]
        estado = aprendiz[4]
        resultado = aprendiz[5]



        nombre_label = tk.Label(root, text=nombre)
        nombre_label.grid(row=i, column=0)

        edad_label = tk.Label(root, text=edad)
        edad_label.grid(row=i, column=1)

        ficha_label = tk.Label(root, text=ficha)
        ficha_label.grid(row=i, column=2)

        estado_label = tk.Label(root, text=estado)
        estado_label.grid(row=i, column=3)

        resultado_label = tk.Label(root, text=resultado)
        resultado_label.grid(row=i, column=4)

def consultar_alumnos_planes():
    ocultar_todo()
    aprendicez_competencia = aprendiz_controller.get_aprendicez_por_plan()

    encabezados = ['Aprendiz','Competencia']
    for i, encabezado in enumerate(encabezados):
        label = tk.Label(root, text=encabezado)
        label.grid(row=0, column=i)

    for i, aprendiz_competencia in enumerate(aprendicez_competencia, start=1):
        aprendiz_com = aprendiz_competencia[0]
        competencia_com = aprendiz_competencia[1]
   

        aprendiz_label = tk.Label(root, text=aprendiz_com)
        aprendiz_label.grid(row=i, column=0)
        competencia_label = tk.Label(root, text=competencia_com)
        competencia_label.grid(row=i, column=1)

  



def consultar_resultado_aprendizaje():
    modificar_cmb_Resultados()
    ocultar_todo()
    lblResultado.grid()
    cmbResultado.grid()
    btnConsultarResultado.grid()

def consultar_resultados():
    modificar_cmb_Resultados()
    ocultar_todo()

    resultados_nombres = resultado_controller.get_resultados_for_table()
    print(resultados_nombres)
    

    # Crear una tabla con encabezados
    encabezados = ['Resultado','Competencia']
    for i, encabezado in enumerate(encabezados):
        label = tk.Label(root, text=encabezado)
        label.grid(row=0, column=i)

    # Mostrar los datos de los estudiantes en la tabla
    for i, resultado_nombre in enumerate(resultados_nombres, start=1):
        nombre = resultado_nombre[0]
        competencia = resultado_nombre[1]
   

        nombre_label = tk.Label(root, text=nombre)
        nombre_label.grid(row=i, column=0)
        competencia_label = tk.Label(root, text=competencia)
        competencia_label.grid(row=i, column=1)

  


def agregar_resultado():
    modificar_cmb_Competencias()

    ocultar_todo()

    lblResultado.grid()
    entResultado.grid(padx=10, pady=10, ipady=20) 
    lblCompetencia.grid()
    cmbCompetencias.grid()
    btnRegistrar.grid()

def registrar_resultado_bd():
    resultado_controller.set_resultado(resultado.get(),diccionarioCompetencias[opcion_seleccionada_competencia.get()])
    mostrar_mensaje()

def consultar_resultado_Actividades_bd():
    # Obtener actividades asociadas al resultado seleccionado
    actividades = resultado_actividad_controller.obtener_actividades_por_resultado(diccionarioResultados[opcion_seleccionada_resultado.get()])
    
    # Limpiar el widget de texto
    text.grid()
    text.delete('1.0', tk.END)

    # Encabezados
    text.insert(tk.END, "Nombre - Nota - Estado\n")
    
    if actividades is not None:
        for actividad in actividades:
            nombre = actividad[1]
            nota = actividad[2] if actividad[2] is not None else "Sin nota" 
            estado = actividad[3] # Si la nota es None, establece un mensaje predeterminado
            text.insert(tk.END, f"{nombre} - {nota} - {estado}\n")  # Usando f-string para formatear la salida
    else:
        text.insert(tk.END, "No se encontraron actividades para este resultado.\n")
        
  
    




    


root = tk.Tk()
root.title("Sena")
root.geometry("400x400")
menu = tk.Menu(root)
root.config(menu=menu)

lblNombre = tk.Label(text='Nombre: ')
lblEdad = tk.Label(text='Edad: ')
lblFicha = tk.Label(text='Ficha: ')
lblMensaje = tk.Label(text='')
lblResultado = tk.Label(text='Resultado: ')
lblCompetencia = tk.Label(text='Competencia: ')
lblNota = tk.Label(text="Nota")
lblActividad = tk.Label(text="Actividad: ")
lblPlanMejoramiento = tk.Label(text="Plan de Mejoramiento: ")
lblFechaEntrega = tk.Label(text="Fecha Entrega: ")
lblDescripcion = tk.Label(text="Descripcion: ")
lblRetroalimentacion = tk.Label(text="Retroalimentacion: ")
lblAviso = tk.Label(text="El Aprendiz No aprobo ninguno de los planes de mejoramiento por ende sera  citado a comite  ")
lblMensajeExito = tk.Label(text="El Resultado a sido aprobado")




opcion_seleccionada = tk.StringVar()
opcion_seleccionada_plan = tk.StringVar()
nombre = tk.StringVar()
edad = tk.StringVar()
resultado = tk.StringVar()
nota = tk.StringVar()
plan = tk.StringVar()
descripcion = tk.StringVar()
retroalimentacion = tk.StringVar()



opcion_seleccionada_resultado = tk.StringVar()
opcion_seleccionada_competencia =  tk.StringVar()
opcion_seleccionada_actividad =  tk.StringVar()
opcion_seleccionada_actividad_filtrada = tk.StringVar()
opcion_seleccionada_resultado_filtrados = tk.StringVar()


entNombre = tk.Entry(root, textvariable=nombre)
entEdad = tk.Entry(root,textvariable=edad)
entResultado = tk.Entry(root,textvariable=resultado,width=45,font=("Times New Roman", 12))
entNota = tk.Entry(root, textvariable=nota)
entPlan = tk.Entry(root, textvariable=plan)
entDescipcion = tk.Entry(root, textvariable=descripcion)
entRetroalimetacion =  tk.Entry(root, textvariable=retroalimentacion,width=68)


datEntrega = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)


fichas = ficha_controller.get_fichas()

cmbFicha = ttk.Combobox(root, values= [ficha[1] for ficha in fichas], textvariable=opcion_seleccionada)
diccionarioFichas = {ficha[1]: ficha[0] for ficha in  fichas}

resultados = resultado_controller.get_resultados()

cmbResultado = ttk.Combobox(root, values= [resultado[1] for resultado in resultados], textvariable=opcion_seleccionada_resultado)
diccionarioResultados = {resultado[1]: resultado[0] for resultado in  resultados}




planes_mejoramiento = plan_mejoramiento_controller.get_planes()



CmbPlanMejoramiento = ttk.Combobox(root, values= [plan_mejoramiento[1] for plan_mejoramiento in planes_mejoramiento], textvariable=opcion_seleccionada_plan)
diccionarioPlanesMejoramiento = {plan_mejoramiento[1]: plan_mejoramiento[0] for plan_mejoramiento in  planes_mejoramiento}
CmbPlanMejoramiento.bind("<<ComboboxSelected>>", cambio_plan_mejoramiento)



cmbActividadesFiltradas =  ttk.Combobox(root,  textvariable=opcion_seleccionada_actividad_filtrada,)


competencias = competencia_controller.get_competencias()
cmbCompetencias = ttk.Combobox(root, values= [competencia[1] for competencia in competencias], textvariable=opcion_seleccionada_competencia)
diccionarioCompetencias = {competencia[1]: competencia[0] for competencia in  competencias}

actividades = actividad_controller.get_actividades()
cmbActividades = ttk.Combobox(root, values= [actividad[1] for actividad in actividades], textvariable=opcion_seleccionada_actividad)
diccionarioActividades = {actividad[1]: actividad[0] for actividad in  actividades}


text = tk.Text()

btnAgregar = tk.Button(text="Agregar", command=agregar_aprendiz_bd)
btnAgregarActividad = tk.Button(text="Agregar", command=agregar_actividad_bd)
btnCalificar = tk.Button(text="Calificar", command=calificar_actividad_bd)
btnRegistrar = tk.Button(text="Registrar", command=registrar_resultado_bd)
btnConsultarResultado = tk.Button(text="Consultar", command=consultar_resultado_Actividades_bd)
btnAgregarPlanMejoramiento = tk.Button(text="Agregar", command=agregar_plan_bd)
btnCalificarPlan = tk.Button(text="Calificar", command=calificar_plan_bd)
btnRetroalimentacion = tk.Button(text="Agregar Retroalimentacion", command=agregar_retroalimentacion_bd)


funcionesAprendiz = tk.Menu(menu)
menu.add_cascade(label="Aprendiz", menu=funcionesAprendiz)
funcionesAprendiz.add_command(label="Agregar Estudiante", command=agregar_aprendiz)
funcionesAprendiz.add_command(label="Consultar Estudiantes", command=consultar_estudiantes)




funcionesResultados = tk.Menu(menu)
menu.add_cascade(label="Resultados De Aprendizaje", menu=funcionesResultados)
funcionesResultados.add_command(label="Agregar Resultado", command=agregar_resultado)
funcionesResultados.add_command(label="Consultar Resultados", command=consultar_resultados)
funcionesResultados.add_command(label="Consultar Resultado de Aprendizaje", command=consultar_resultado_aprendizaje)



funcionesActividades = tk.Menu(menu)
menu.add_cascade(label="Actividades", menu=funcionesActividades)
funcionesActividades.add_command(label="Agregar Actividad", command=agregar_actividad)
funcionesActividades.add_command(label="Calificar Actividad", command=calificar_actividad)

funcionesActividades.add_command(label="Consultar Actividades", command=consultar_actividades)


funcionesPlanMejoramiento = tk.Menu(menu)
menu.add_cascade(label="Planes de Mejoramiento", menu=funcionesPlanMejoramiento)
funcionesPlanMejoramiento.add_command(label="Calificar Plan de Mejoramiento", command=calificar_plan)
funcionesPlanMejoramiento.add_command(label="Consultar Alumnos con planes de mejoramiento", command=consultar_alumnos_planes)







root.mainloop()
