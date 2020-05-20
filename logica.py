#Johan David Gomez Gil
#Sebastian Bustamante
#Lenguajes 2 
#2020


from datos import *
from tkinter import *

class Logica:

    datos = Datos()  

    def getEnfermedades(self):
        consulta = 'SELECT * FROM Enfermedad'
        filas = self.datos.ejecutarConsulta(consulta)
        enfermedades = []
        for fila in filas:
            enfermedades.append(fila[1])
        return enfermedades


    def asignarEnfermedad(self,enfermedades,agregadas):
        indice = enfermedades.curselection() #Devuelve un diccionario con la posicion del elemento
        seleccion = (enfermedades.get(indice[0])) #Devuelve el valor en el indice
        agregadas.insert(0,seleccion)
        enfermedades.delete(indice[0])

    def quitarEnfermedad(self, enfermedades, agregadas):
        indice = agregadas.curselection()
        seleccion = (agregadas.get(indice[0]))
        enfermedades.insert(0,seleccion)
        agregadas.delete(indice[0])

    def getSintomas(self):
        consulta = 'SELECT * FROM Sintoma'
        filas = self.datos.ejecutarConsulta(consulta)
        sintomas = []
        for fila in filas:
            sintomas.append(fila[1])
        return sintomas

    def asignarSintoma(self,sintomas,agregados):
        indice = sintomas.curselection()
        seleccion = sintomas.get(indice[0])
        agregados.insert(0, seleccion)
        sintomas.delete(indice[0])

    def quitarSintoma(self,sintomas,agregados):
        indice = agregados.curselection()
        seleccion = agregados.get(indice[0])
        sintomas.insert(0, seleccion)
        agregados.delete(indice[0])

#------------------------------Guardar todos los datos del paciente-------------------------

    def crearPaciente(self,datosPaciente,agregadas,agregados,anoRegistro,mesResgistro,diaRegistro,temperatura):

            
        crearPaciente = 'INSERT INTO Paciente VALUES(?,?,?,?,?,?,?,?,?,?)'
        self.datos.ejecutarConsulta(crearPaciente, datosPaciente)

        enfermedades = agregadas.get(0,END)
        idenEnfermedad = 'SELECT id FROM Enfermedad WHERE nombre = (?)'
        asignarEnfermedad = 'INSERT INTO PacienteEnfermedad VALUES(?,?)'

        sintomas = agregados.get(0,END)
        idenSintoma = 'SELECT id FROM Sintoma WHERE descripcion = (?)'
        asignarSintoma = 'INSERT INTO PacienteSintoma VALUES(?,?,?,?)'

        for enfermedad in enfermedades:
            param = [enfermedad]
            res = self.datos.ejecutarConsulta(idenEnfermedad,param)
            lista = res.fetchall()
            iden = lista[0][0]
            param = [datosPaciente[0],iden]
            self.datos.ejecutarConsulta(asignarEnfermedad,param)

        fecha =""
        fecha = fecha + anoRegistro.get() + '-'+mesResgistro.get() +'-'+ diaRegistro.get()

        temperatura = temperatura.get()

        for sintoma in sintomas:
            param = [sintoma]
            res = self.datos.ejecutarConsulta(idenSintoma,param)
            lista = res.fetchall()
            iden = lista[0][0]
            param = [datosPaciente[0],iden,fecha,temperatura]
            self.datos.ejecutarConsulta(asignarSintoma,param)

            
#--------------------------------NUEVA ENFERMEDAD-----------------------------------------------------

    def nuevaEnfermedad(self, nombre):

        comprobar = 'SELECT * FROM Enfermedad WHERE nombre = {}'.format(nombre)

        resultados = self.datos.ejecutarConsulta(comprobar)

        res =[]

        for resul in resultados:
            res.append(resul[0])

        print (res)

        insertar = 'INSERT INTO Enfermedad VALUES (NULL,?)'

        parametros = [str(nombre)]
        #self.datos.ejecutarConsulta(insertar,parametros)