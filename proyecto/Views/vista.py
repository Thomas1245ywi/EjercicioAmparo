import tkinter as tk
from Controllers.FichaController import FichaController
from Controllers.ProgramaController import ProgramaController
from Controllers.AprendizController import AprendizController
from Controllers.ResultadoController import ResultadoController
from Controllers.CompetenciaController import CompetenciaController
from Controllers.EstadoController import EstadoController
from Controllers.ActividadController import ActividadController
from Controllers.EstadoController import EstadoController





from tkinter import ttk
ficha_controller = FichaController()
programa_controller = ProgramaController()
aprendiz_controller = AprendizController()
resultado_controller = ResultadoController()
competencia_controller = CompetenciaController()
estado_controller = EstadoController() 
actividad_controller = ActividadController() 





def agregar_aprendiz_bd():

    aprendiz_controller.set_aprendiz(nombre.get(),edad.get(), diccionarioFichas[opcion_seleccionada.get()], diccionarioResultados[opcion_seleccionada_resultado.get()])


def ocultar_todo():
   
    for widget in root.winfo_children():
        widget.grid_forget()

def calificar_actividad_bd():
    actividad_controller.calificar_actividad(diccionarioActividades[opcion_seleccionada_actividad.get()],nota.get())

def agregar_actividad_bd():
    actividad_controller.set_actividad(nombre.get(),diccionarioResultados[cmbResultado.get()])
    
def agregar_actividad():
    ocultar_todo()
    lblNombre.grid()
    entNombre.grid()
    lblResultado.grid()
    cmbResultado.grid()
    btnAgregarActividad.grid()

def consultar_actividades():
    pass
                      

def calificar_actividad():
    ocultar_todo()
    lblActividad.grid()
    cmbActividades.grid()
    lblNota.grid()
    entNota.grid()
    btnCalificar.grid()

def agregar_aprendiz():
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

    aprendicez = aprendiz_controller.get_aprendicez()

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

def consultar_resultados():
    ocultar_todo()

    resultados = resultado_controller.get_resultados()

    # Crear una tabla con encabezados
    encabezados = ['Resultado','Competencia']
    for i, encabezado in enumerate(encabezados):
        label = tk.Label(root, text=encabezado)
        label.grid(row=0, column=i)

    # Mostrar los datos de los estudiantes en la tabla
    for i, resultado in enumerate(resultados, start=1):
        nombre = resultado[1]
        competencia = resultado[2]
   

        nombre_label = tk.Label(root, text=nombre)
        nombre_label.grid(row=i, column=0)
        competencia_label = tk.Label(root, text=competencia)
        competencia_label.grid(row=i, column=1)

  


def agregar_resultado():

    ocultar_todo()
    lblResultado.grid()
    entResultado.grid(padx=10, pady=10, ipady=20) 
    lblCompetencia.grid()
    cmbCompetencias.grid()
    btnRegistrar.grid()

def registrar_resultado_bd():
    resultado_controller.set_resultado(resultado.get(),diccionarioCompetencias[opcion_seleccionada_competencia.get()])


    

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


opcion_seleccionada = tk.StringVar()
nombre = tk.StringVar()
edad = tk.StringVar()
resultado = tk.StringVar()
nota = tk.StringVar()

opcion_seleccionada_resultado = tk.StringVar()
opcion_seleccionada_competencia =  tk.StringVar()
opcion_seleccionada_actividad =  tk.StringVar()


entNombre = tk.Entry(root, textvariable=nombre)
entEdad = tk.Entry(root,textvariable=edad)
entResultado = tk.Entry(root,textvariable=resultado,width=45,font=("Times New Roman", 12))
entNota = tk.Entry(root, textvariable=nota)

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




btnAgregar = tk.Button(text="Agregar", command=agregar_aprendiz_bd)
btnAgregarActividad = tk.Button(text="Agregar", command=agregar_actividad_bd)
btnCalificar = tk.Button(text="Calificar", command=calificar_actividad_bd)
btnRegistrar = tk.Button(text="Registrar", command=registrar_resultado_bd)


funcionesAprendiz = tk.Menu(menu)
menu.add_cascade(label="Aprendiz", menu=funcionesAprendiz)
funcionesAprendiz.add_command(label="Agregar Estudiante", command=agregar_aprendiz)
funcionesAprendiz.add_command(label="Consultar Estudiantes", command=consultar_estudiantes)




funcionesResultados = tk.Menu(menu)
menu.add_cascade(label="Resultados De Aprendizaje", menu=funcionesResultados)
funcionesResultados.add_command(label="Agregar Resultado", command=agregar_resultado)
funcionesResultados.add_command(label="Consultar Resultados", command=consultar_resultados)


funcionesActividades = tk.Menu(menu)
menu.add_cascade(label="Actividades", menu=funcionesActividades)
funcionesActividades.add_command(label="Agregar Actividad", command=agregar_actividad)
funcionesActividades.add_command(label="Calificar Actividad", command=calificar_actividad)

funcionesActividades.add_command(label="Consultar Actividades", command=consultar_actividades)





root.mainloop()
