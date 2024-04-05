import sqlite3 as sql



class AprendizModel:
    def __init__(self):
        
        self.conn = sql.connect("bd_sena.db")
        self.cursor = self.conn.cursor()
 
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Aprendiz (
                id INTEGER PRIMARY KEY,
                nombre TEXT, 
                edad INTEGER,
                id_ficha INTEGER,
                id_estado INTEGER,
                id_resultado INTEGER,
                FOREIGN KEY (id_resultado) REFERENCES Resultado(id)
                FOREIGN KEY(id_ficha) REFERENCES Ficha(id),
                FOREIGN KEY(id_estado) REFERENCES EstadoAprendiz(id)


                                    
            );
                    
        """)



        self.conn.commit()

    def set_aprendiz(self, nombre, edad, id_ficha, id_resultado,estado_name):

        sentencia_estado = 'SELECT id FROM EstadoAprendiz WHERE nombre = ?'
        estado_id = self.conn.execute(sentencia_estado,(estado_name,)).fetchone()
        estado = estado_id[0]
        print(estado)

        if estado:
            # Insertar la actividad en la base de datos
            sentencia = 'INSERT INTO Aprendiz(nombre, edad, id_ficha,id_resultado,id_estado) VALUES (?,?,?,?,?)'
            self.cursor.execute(sentencia, (nombre, edad, id_ficha,id_resultado,estado))
            self.conn.commit()
            print("Actividad agregada exitosamente.")
        else:
            print(f"No se encontró un estado con el nombre '{estado}'. No se pudo agregar la actividad.")
       

    def get_aprendicez(self):
        self.cursor.execute('SELECT * FROM  Aprendiz')
        return self.cursor.fetchall()
    

    def get_aprendicez_for_table(self):
        self.cursor.execute('SELECT Aprendiz.id,Aprendiz.nombre,Aprendiz.edad, Ficha.numero, EstadoAprendiz.nombre, Resultado.nombre FROM  Aprendiz INNER JOIN Ficha ON id_ficha = Ficha.id INNER JOIN EstadoAprendiz ON id_estado = EstadoAprendiz.id  INNER JOIN Resultado ON id_resultado = Resultado.id ')
        return self.cursor.fetchall()

    def obtener_actividades_por_alumno(self, id_alumno):
        sentencia = 'SELECT id_resultado FROM Alumno WHERE id = ?'
        self.cursor.execute(sentencia, (id_alumno,))
        resultado_aprendizaje = self.cursor.fetchone()

        if resultado_aprendizaje:
            id_resultado_aprendizaje = resultado_aprendizaje[0]
            # 2. Consultar las actividades asociadas al resultado de aprendizaje
            sentencia_actividades = 'SELECT * FROM Actividad WHERE id_resultado = ?'
            self.cursor.execute(sentencia_actividades, (id_resultado_aprendizaje,))
            actividades = self.cursor.fetchall()

            if actividades:
                return actividades
            else:
                print("No se encontraron actividades asociadas al resultado de aprendizaje del alumno.")
        else:
            print("No se encontró resultado de aprendizaje para el alumno.")

    def cerrar_conexion(self):
        self.conn.close()









