import tkinter as tk
from Controllers.FichaController import FichaController
from Controllers.ProgramaController import ProgramaController
from Controllers.AprendizController import AprendizController
from Controllers.ResultadoController import ResultadoController


from tkinter import ttk
ficha_controller = FichaController()
programa_controller = ProgramaController()
aprendiz_controller = AprendizController()
resultado_controller = ResultadoController()



def agregar_aprendiz_bd():

    aprendiz_controller.set_aprendiz(nombre.get(),edad.get(), diccionarioFichas[opcion_seleccionada.get()], diccionarioResultados[opcion_seleccionada_resultado.get()]
                        
    
)


def ocultar_todo():
   
    for widget in root.winfo_children():
        widget.grid_forget()


   



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
    encabezados = ['Resultado']
    for i, encabezado in enumerate(encabezados):
        label = tk.Label(root, text=encabezado)
        label.grid(row=0, column=i)

    # Mostrar los datos de los estudiantes en la tabla
    for i, aprendiz in enumerate(resultados, start=1):
        nombre = aprendiz[1]
   

        nombre_label = tk.Label(root, text=nombre)
        nombre_label.grid(row=i, column=0)

  


def agregar_resultado():

    ocultar_todo()
    lblResultado.grid()
    entResultado.grid(padx=10, pady=10, ipady=20) 
    btnRegistrar.grid()

def registrar_resultado_bd():
    resultado_controller.set_resultado(resultado.get())


    

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


opcion_seleccionada = tk.StringVar()
nombre = tk.StringVar()
edad = tk.StringVar()
resultado = tk.StringVar()
opcion_seleccionada_resultado = tk.StringVar()



entNombre = tk.Entry(root, textvariable=nombre)
entEdad = tk.Entry(root,textvariable=edad)
entResultado = tk.Entry(root,textvariable=resultado,width=45,font=("Times New Roman", 12))

fichas = ficha_controller.get_fichas()

cmbFicha = ttk.Combobox(root, values= [ficha[1] for ficha in fichas], textvariable=opcion_seleccionada)
diccionarioFichas = {ficha[1]: ficha[0] for ficha in  fichas}

resultados = resultado_controller.get_resultados()

cmbResultado = ttk.Combobox(root, values= [resultado[1] for resultado in resultados], textvariable=opcion_seleccionada_resultado)
diccionarioResultados = {resultado[1]: resultado[0] for resultado in  resultados}

btnAgregar = tk.Button(text="Agregar", command=agregar_aprendiz_bd)
btnRegistrar = tk.Button(text="Registrar", command=registrar_resultado_bd)


funcionesAprendiz = tk.Menu(menu)
menu.add_cascade(label="Aprendiz", menu=funcionesAprendiz)
funcionesAprendiz.add_command(label="Agregar Estudiante", command=agregar_aprendiz)
funcionesAprendiz.add_command(label="Consultar Estudiantes", command=consultar_estudiantes)

funcionesResultados = tk.Menu(menu)
menu.add_cascade(label="Resultados De Aprendizaje", menu=funcionesResultados)
funcionesResultados.add_command(label="Agregar Resultado", command=agregar_resultado)
funcionesResultados.add_command(label="Consultar Resultadors", command=consultar_resultados)







# def listar_contactos():
    
#     frame_agregar_contacto.grid_forget()

#     text_area.delete('1.0',tk.END)
#     contactos = ct.listar_contactos()

#     frame_contactos_botones.grid_forget()
#     frame_contactos_botones.grid()

#     # Mostrar botones para cada contacto en la lista
#     for contacto in contactos:
#         text_area.insert(tk.END, contacto)
#         text_area.insert("Acciones", frame_contactos_botones)


#         btn_borrar = tk.Button(frame_contactos_botones, text='Borrar' )
#         btn_borrar.grid(side="right")
#         btn_editar = tk.Button(frame_contactos_botones, text='Editar')
#         btn_editar.grid(side="left")

      
#     text_area.grid()

#     frame_contactos.grid()





# def agregar_contacto(nombre, numero):
#     contacto = ct.Contacto(nombre, numero)
#     lbl_exitoso.config(text=contacto.agregar_contacto())
#     listar_contactos()










# def ver_agregar_contacto():
    
#     frame_contactos.grid_forget()
    
    

#     lbl_nombre.grid()
#     ent_nombre.grid()
#     lbl_numero.grid()
#     ent_numero.grid()
#     btn_agregar.grid()
#     frame_agregar_contacto.grid()

    


    

# menu = tk.Menu(root)
# root.config(menu=menu)



# opciones = tk.Menu(menu)
# menu.add_cascade(label="Opciones", menu=opciones)

# opciones.add_command(label="Listar Contacto",command = listar_contactos)
# opciones.add_command(label="Agregar Contacto",command = ver_agregar_contacto)
# opciones.add_command(label="Modificar Contacto",command = '')





root.mainloop()
