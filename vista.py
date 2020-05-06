from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import sqlite3


class ventana:

    database = 'BDD.db'

    paises = ['Colombia','Ecuador','Estados unidos','Mexico','Panama','Venezuela']

    def __init__(self, ventana):
        self.wind = ventana
        self.wind.title('Pacientes')

        frame = LabelFrame(self.wind, text = 'DATOS DEL PACIENTE')
        frame.grid(row = 0, column = 0, padx = 6, pady = 20)

        frameEnfermedades = LabelFrame(self.wind, text = 'ENFERMEDADES QUE PADECE')
        frameEnfermedades.grid(row = 0, column = 1, padx = 6, pady = 20)

        frameSintomas = LabelFrame(self.wind, text = 'SINTOMAS DEL PACIENTE')
        frameSintomas.grid(row = 0, column = 2, padx = 6, pady = 20)

        frameFecha = LabelFrame(self.wind, text = 'FECHA DE REGISTRO')
        frameFecha.grid(row = 1, column = 1)

        #--------------------------Menu--------------------------------------------

        self.barraMenu = Menu(self.wind)
        self.wind.config(menu = self.barraMenu)

        self.archivo = Menu(self.barraMenu, tearoff = 0)
        self.archivo.add_command(label = 'Nueva enfermedad' )
        self.archivo.add_command(label = 'Nuevo sintoma')
        self.archivo.add_command(label = 'Exportar')
        self.archivo.add_command(label = 'Salir', command = self.wind.destroy)

        self.editar = Menu(self.barraMenu, tearoff = 0)
        self.editar.add_command(label = 'Editar pacientes')
        self.editar.add_command(label = 'Editar enfermedades')
        self.editar.add_command(label = 'Editar sintomas')

        self.ver = Menu(self.barraMenu, tearoff = 0)
        self.ver.add_command(label = 'Graficar')
        self.ver.add_command(label = 'Ver pacientes')
        self.ver.add_command(label = 'Ver enfermedades')
        self.ver.add_command(label = 'Ver sintomas')
        self.subVer = Menu(self.ver, tearoff = 0)
        self.subVer.add_command(label = 'Pacientes con mayor riesgo')
        self.subVer.add_command(label = 'Pacientes con fiebre >= 38')
        self.ver.add_cascade(label = 'Consultas...', menu = self.subVer)


        self.barraMenu.add_cascade(label ='Archivo', menu = self.archivo)
        self.barraMenu.add_cascade(label = 'Editar', menu = self.editar)
        self.barraMenu.add_cascade(label = 'Ver', menu = self.ver)

        #------------Nombre---------------------------------------

        Label(frame, text = 'Nombre completo: ').grid(row = 1, column = 0)
        self.nombre = ttk.Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1, pady =1)

        #------------Tipo de documento---------------------------

        Label(frame, text = 'Tipo de documento: ').grid(row = 2, column = 0)
        self.tipoDocumento = ttk.Combobox(frame)
        self.tipoDocumento["values"] = ['Cedula','T.I','Pasaporte']
        self.tipoDocumento.grid(row = 2, column = 1, pady =1)

        #------------Numero de documento de documento---------------------------

        Label(frame, text = 'Numero de documento: ').grid(row = 3, column = 0)
        self.numDocumento = ttk.Entry(frame)
        self.numDocumento.grid(row = 3, column = 1, pady =1)

        #------------Genero---------------------------------------------

        Label(frame, text = 'Genero: ').grid(row = 4, column = 0)
        self.genero = ttk.Combobox(frame, state ="readonly")
        self.genero["values"] = ['F','M']
        self.genero.grid(row = 4, column = 1, pady =1)

        #------------Barrio------------------------------------------------

        Label(frame, text = 'Barrio: ').grid(row = 5, column = 0)
        self.barrio = ttk.Entry(frame)
        self.barrio.grid(row = 5, column = 1, pady =1)

        #-------------Ciudad------------------------------------------------

        Label(frame, text = 'Ciudad: ').grid(row = 6, column = 0)
        self.ciudad = ttk.Entry(frame)
        self.ciudad.grid(row = 6, column = 1, pady =1)

        #--------------Telefono----------------------------------------------

        Label(frame, text = 'Telefono: ').grid(row = 7, column = 0)
        self.telefono = ttk.Entry(frame)
        self.telefono.grid(row = 7, column = 1, pady =1)

        #--------------Año de nacimiento---------------------------------------

        Label(frame, text = 'Año de nacimiento: ').grid(row = 8, column = 0)
        self.ano = ttk.Entry(frame)
        self.ano.grid(row = 8, column = 1, pady =1)

        #--------------Profesion----------------------------------------------

        Label(frame, text = 'Profesión: ').grid(row = 9, column = 0)
        self.profesion = ttk.Entry(frame)
        self.profesion.grid(row = 9, column =1, pady =1)

        #--------------Nacionalidad----------------------------------------------

        Label(frame, text = 'Nacionalidad').grid(row = 10, column = 0)
        self.nacionalidad = ttk.Combobox(frame)
        self.nacionalidad["values"] = self.paises
        self.nacionalidad.grid(row = 10, column = 1, pady =1)
        #valor = self.nacionalidad.get()

        #-----------------Fecha------------------------------------------------------------

        Label(frameFecha, text = 'Año: ').grid(row = 0, column = 0)
        self.anoRegistro = ttk.Entry(frameFecha)
        self.anoRegistro.grid(row=0, column =1)
        Label(frameFecha, text = 'Mes: ').grid(row = 1, column = 0)
        self.mesResgistro = ttk.Entry(frameFecha)
        self.mesResgistro.grid(row = 1, column = 1)
        Label(frameFecha, text = 'Dia: ').grid(row = 2, column = 0)
        self.diaRegistro = ttk.Entry(frameFecha)
        self.diaRegistro.grid(row =2, column =1)

        #-----------------Temperatura-------------------------------------------------------
         
        Label(frame, text = 'Temperatura: ').grid(row = 11, column = 0)
        self.temperatura = ttk.Entry(frame)
        self.temperatura.grid(row = 11, column = 1, pady = 1)


        #--------------Asignar enfermedades----------------------------------------------

        Label(frameEnfermedades, text = 'Enfermedades: ').grid(row = 11, column = 0)
        Label(frameEnfermedades, text = 'Asignadas: ').grid(row = 11, column = 1)
        self.enfermedades = Listbox(frameEnfermedades)
        self.enfermedades.insert(0, * self.getEnfermedades())
        self.enfermedades.grid(row = 12, column = 0)
        
        self.agregadas = Listbox(frameEnfermedades)
        self.agregadas.grid(row = 12, column = 1)

        ttk.Button(frameEnfermedades, text = 'Asignar', command = self.asignarEnfermedad).grid(row = 13, column = 0)
        ttk.Button(frameEnfermedades, text = 'Quitar', command = self.quitarEnfermedad).grid(row = 13, column = 1)

        #----------------asignar sintomas-----------------------------------------

        Label(frameSintomas, text = 'Sintomas: ').grid(row =1, column=0)
        Label(frameSintomas, text = 'Asignados: ').grid(row = 1, column = 1)
        self.sintomas = Listbox(frameSintomas)
        self.sintomas.insert(0, *self.getSintomas())
        self.sintomas.grid(row = 2, column = 0)

        self.agregados = Listbox(frameSintomas)
        self.agregados.grid(row = 2, column =1)



        ttk.Button(frameSintomas, text = 'Asignar', command = self.asignarSintoma).grid(row = 3, column = 0)
        ttk.Button(frameSintomas, text = 'Quitar', command = self.quitarSintoma).grid(row = 3, column = 1)



        #--------------Boton crear paciente-----------------------

        ttk.Button(self.wind, text = 'Registrar', command = self.crearPaciente).grid(row = 1, column =2, 
        pady = 3, rowspan = 3, sticky = W + E )

    #------------------------Funciones-----------------------------------------------------------------   

    def ejecutarConsulta(self,consulta, parametros = ()):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            resultados = cursor.execute(consulta, parametros)
            conn.commit()
        return resultados

    def getEnfermedades(self):
        consulta = 'SELECT * FROM Enfermedad'
        filas = self.ejecutarConsulta(consulta)
        enfermedades = []
        for fila in filas:
            enfermedades.append(fila[1])
        return enfermedades


    def asignarEnfermedad(self):
        indice = self.enfermedades.curselection() #Devuelve un diccionario con la posicion del elemento
        seleccion = (self.enfermedades.get(indice[0])) #Devuelve el valor en el indice
        self.agregadas.insert(0,seleccion)
        self.enfermedades.delete(indice[0])

    def quitarEnfermedad(self):
        indice = self.agregadas.curselection()
        seleccion = (self.agregadas.get(indice[0]))
        self.enfermedades.insert(0,seleccion)
        self.agregadas.delete(indice[0])

    def getSintomas(self):
        consulta = 'SELECT * FROM Sintoma'
        filas = self.ejecutarConsulta(consulta)
        sintomas = []
        for fila in filas:
            sintomas.append(fila[1])
        return sintomas

    def asignarSintoma(self):
        indice = self.sintomas.curselection()
        seleccion = self.sintomas.get(indice[0])
        self.agregados.insert(0, seleccion)
        self.sintomas.delete(indice[0])

    def quitarSintoma(self):
        indice = self.agregados.curselection()
        seleccion = self.agregados.get(indice[0])
        self.sintomas.insert(0, seleccion)
        self.agregados.delete(indice[0])

#------------------------------Guardar todos los datos del paciente-------------------------

    def crearPaciente(self):
        try:
        
            datosPaciente = [self.numDocumento.get(), self.tipoDocumento.get(),
            self.nombre.get(), self.genero.get(),self.barrio.get(),self.ciudad.get(),
            self.telefono.get(),self.ano.get(), self.profesion.get(), self.nacionalidad.get()]

            crearPaciente = 'INSERT INTO Paciente VALUES(?,?,?,?,?,?,?,?,?,?)'
            self.ejecutarConsulta(crearPaciente, datosPaciente)

            enfermedades = self.agregadas.get(0,END)
            idenEnfermedad = 'SELECT id FROM Enfermedad WHERE nombre = (?)'
            asignarEnfermedad = 'INSERT INTO PacienteEnfermedad VALUES(?,?)'

            sintomas = self.agregados.get(0,END)
            idenSintoma = 'SELECT id FROM Sintoma WHERE descripcion = (?)'
            asignarSintoma = 'INSERT INTO PacienteSintoma VALUES(?,?,?,?)'

            for enfermedad in enfermedades:
                param = [enfermedad]
                res = self.ejecutarConsulta(idenEnfermedad,param)
                lista = res.fetchall()
                iden = lista[0][0]
                param = [datosPaciente[0],iden]
                self.ejecutarConsulta(asignarEnfermedad,param)

            fecha =""
            fecha = fecha + self.anoRegistro.get() + '-'+self.mesResgistro.get() +'-'+ self.diaRegistro.get()
            temperatura = self.temperatura.get()

            for sintoma in sintomas:
                param = [sintoma]
                res = self.ejecutarConsulta(idenSintoma,param)
                lista = res.fetchall()
                iden = lista[0][0]
                param = [datosPaciente[0],iden,fecha,temperatura]
                self.ejecutarConsulta(asignarSintoma,param)

            messagebox.showinfo(message = 'Registro guardado satisfactoriamente', title = 'Registro guardado')
        except sqlite3.OperationalError as errorSQL:
            mensaje = errorSQL
            messagebox.showerror(message = mensaje, title = 'Error')
        except:
            messagebox.showerror(message = 'Ha ocurrido un error inesperado', title = 'Error')

        

        

        
        
        