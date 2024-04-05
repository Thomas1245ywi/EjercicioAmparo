import tkinter as tk
from Controllers.FichaController import FichaController
from Controllers.ProgramaController import ProgramaController
from Controllers.AprendizController import AprendizController
from Controllers.ResultadoController import ResultadoController
from Controllers.CompetenciaController import CompetenciaController
from Controllers.EstadoController import EstadoController
from Controllers.EstadoAprendizController import EstadoAprendizController

from Controllers.ActividadController import ActividadController
from Controllers.ResultadoActividadController import ResultadoActividadController

from Controllers.EstadoController import EstadoController
from Controllers.PlanMejoramientoController import PlanMejoramientoController








from tkinter import ttk
ficha_controller = FichaController()
programa_controller = ProgramaController()
aprendiz_controller = AprendizController()
resultado_controller = ResultadoController()
competencia_controller = CompetenciaController()
estado_controller = EstadoController() 
actividad_controller = ActividadController() 
estado_controller = EstadoAprendizController() 
resultado_actividad_controller = ResultadoActividadController()
plan_mejoramiento_controller = PlanMejoramientoController()

actividades_arreglo = []



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


def ocultar_todo():
   
    for widget in root.winfo_children():
        widget.grid_forget()

def calificar_actividad_bd():
    global actividades_arreglo
    actividades_arreglo = actividad_controller.calificar_actividad(diccionarioActividades[opcion_seleccionada_actividad.get()],nota.get())
    if actividades_arreglo != []:
        ocultar_todo()
        lblPlanMejoramiento.grid()
        entPlan.grid()
        btnAgregarPlanMejoramiento.grid()




        

def agregar_actividad_bd():
    actividad_controller.set_actividad(nombre.get())
    modificar_cmb_Actividades()
    resultado_actividad_controller.agregar_relacion_resultado_actividad(diccionarioResultados[opcion_seleccionada_resultado.get()],    diccionarioActividades[nombre.get()]
)

    
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
    resultados_pet = []

    
    for actividad in actividades:
        resultado_pet = resultado_actividad_controller.obtener_resultado_por_actividad(actividad[0])
        resultados_pet.append(resultado)

    resultadosConjunto = set(resultado_pet)
    primer_resultado = resultadosConjunto.pop()

    print(primer_resultado)

    plan_mejoramiento_controller.set_plan(plan.get(),int(primer_resultado))


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

def consultar_resultado_Actividades_bd():
    # Obtener actividades asociadas al resultado seleccionado
    actividades = resultado_actividad_controller.obtener_actividades_por_resultado(diccionarioResultados[opcion_seleccionada_resultado.get()])
    text.grid()
    # Limpiar el widget de texto
    text.delete('1.0', tk.END)
    
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
lblPlanMejoramiento = tk.Label(text="El alumno a perdido una de las actividades Ingrese el nombre del Plan de Mejoramiento: ")



opcion_seleccionada = tk.StringVar()
nombre = tk.StringVar()
edad = tk.StringVar()
resultado = tk.StringVar()
nota = tk.StringVar()
plan = tk.StringVar()


opcion_seleccionada_resultado = tk.StringVar()
opcion_seleccionada_competencia =  tk.StringVar()
opcion_seleccionada_actividad =  tk.StringVar()


entNombre = tk.Entry(root, textvariable=nombre)
entEdad = tk.Entry(root,textvariable=edad)
entResultado = tk.Entry(root,textvariable=resultado,width=45,font=("Times New Roman", 12))
entNota = tk.Entry(root, textvariable=nota)
entPlan = tk.Entry(root, textvariable=plan)

fichas = ficha_controller.get_fichas()

cmbFicha = ttk.Combobox(root, values= [ficha[1] for ficha in fichas], textvariable=opcion_seleccionada)
diccionarioFichas = {ficha[1]: ficha[0] for ficha in  fichas}

resultados = resultado_controller.get_resultados()

cmbResultado = ttk.Combobox(root, values= [resultado[1] for resultado in resultados], textvariable=opcion_seleccionada_resultado)
diccionarioResultados = {resultado[1]: resultado[0] for resultado in  resultados}


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





root.mainloop()
