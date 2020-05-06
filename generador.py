#Johan David Gomez Gil
# Lenguajes 2 
#2020

import random
import sqlite3

nombre = ['MARIA','MARIA CARMEN','JOSEFA','ISABEL','MARIA DOLORES','CARMEN',
'FRANCISCA','MARIA PILAR','DOLORES','MARIA JOSE','ANTONIA','ANA','MARIA ISABEL',
'MARIA ANGELES','PILAR','ANA MARIA','LUCIA','CRISTINA','LAURA','ENCARNACION','JUANA','MARIA TERESA','ROSARIO','ELENA','MARTA',
'MANUELA','ROSA MARIA','MARIA LLANOS','MARIA JOSEFA','RAQUEL','ANGELES','CONCEPCION','MERCEDES','IRENE','TERESA','BEATRIZ',
'PAULA','ANGELA','JULIA','ANA BELEN','ROCIO','AMPARO','ALICIA','CONSUELO','ROSA','ASCENSION','ANDREA',
'MARIA ROSARIO','MARIA JESUS','MARIA LUISA','ANTONIO','JOSE','FRANCISCO','JUAN','MANUEL','PEDRO','JESUS','ANGEL','MIGUEL','JAVIER','JOSE ANTONIO','DAVID',
'CARLOS','JOSE LUIS','ALEJANDRO','MIGUEL ANGEL','FRANCISCO JAVIER','RAFAEL','DANIEL',
'JUAN JOSE','LUIS','PABLO','JUAN ANTONIO','JOAQUIN','SERGIO','FERNANDO', 
'JUAN CARLOS','ANDRES','JOSE MANUEL','JOSE MARIA','RAMON','RAUL','ALBERTO','ENRIQUE','ALVARO','VICENTE',
'EMILIO','FRANCISCO JOSE','DIEGO','JULIAN','JORGE','ALFONSO','ADRIAN', 
'RUBEN','SANTIAGO','IVAN','JUAN MANUEL','PASCUAL','JOSE MIGUEL','MARIO']

apellido = ['MARTINEZ','LOPEZ','SANCHEZ','GONZALEZ','GOMEZ',
'FERNANDEZ','MORENO','JIMENEZ','PEREZ','RODRIGUEZ',
'NAVARRO','RUIZ','DIAZ','SERRANO','HERNANDEZ','MUÑOZ','SAEZ','ROMERO',
'RUBIO','ALFARO','MOLINA','LOZANO','CASTILLO','PICAZO','ORTEGA','MORCILLO',
'CANO','MARIN','CUENCA','GARRIDO','TORRES','CORCOLES','GIL',
'ORTIZ','CALERO','VALERO','CEBRIAN','RODENAS','ALARCON','BLAZQUEZ','NUÑEZ',
'PARDO','MOYA','TEBAR','REQUENA','ARENAS','BALLESTEROS','COLLADO','RAMIREZ',
'VALENCIA']

ciudad = ['Medellín','Abejorral','Abriaquí','Alejandría','Amalfi','Andes','Angelópolis','Angostura',
'Carolina','Caucasia','Chigorodó','Bello','Sabaneta','Barbosa','Copacabana','Dabeiba','Dabeiba','El Bagre',
'Gomez Plata','Girardota','Guadalupe','Guarne',
'Guatape', 'Itagui','Ituango','Jericó','La Unión','La Estrella','La Ceja','Rionegro','Sabanalarga',
'Sabaneta','Santo Domingo', 'Segovia','Taraza','Valdivia','Yarumal','Barranquilla','Sabanalarga']

profesion = ['Actor','Medico','Abogado','Administrador','Antropólogo','Archivero','Arqueólogo','Arquitecto',
'Astrónomo','Atleta','Bacteriólogo','Barrendero','Bibliotecario','Biofísico','Bombero','Botánico',
'Camarero','Cancerólogo','Cardiólogo','Carnicero','Carpintero','Cocinero','Decorador','Odontologo',
'Dermatólogo','Dibujante','Economista','Electricista','Enfermero','Epidemiólogo','Estadista','Farmacéutico',
'Farmacólogo','Fiscal','Físico','Fisioterapeuta','Comerciante','Forense','Fotógrafo','Genetista','Geógrafo',
'Geriatra','Hepatólogo','Ingeniero','Inmunólogo','Juez','Matemático','Mecánico','Microcirujano','Modelo',
'Neumólogo','Neuroanatomista','Neurobiólogo','Neurólogo','Odontólogo','Oftalmólogo','Oncólogo','Panadero',
'Pediatra','Periodista','Piloto de avión','Programador','Psicólogo','Psiquiatra','Recepcionista','Soldado',
'Taxista','Terapeuta','Vendedor','Veterinario','Virólogo','Zoólogo','Zootécnico']

#---------------------Datos del paciente-----------------------------------------------------------

def generarNombre():
    nom = ""
    nom = random.choice(nombre)
    apellido1 = random.choice(apellido)
    apellido2 = random.choice(apellido)
    nom = nom + " " + apellido1 + " " + apellido2
    return nom


def generarEdad():
    #edadas entre 18 y 85
    return random.randint(18, 85)

def generarSexo():
    return random.choice(['F', 'M'])

def generarTipoDocumento():
    return random.choice(['Cedula', 'Pasaporte','Permiso especial', 'Tarjeta de identidad'])

def generarNumDocumento():
    return random.randint(100000, 999999)

def generarBarrio():
    carrera = random.randint(5, 90)
    calle = random.randint(5, 90)
    casa = random.randint(5, 90)
    barrio = "Cra "
    
    barrio = barrio + str(carrera) + " # " + str(calle) + "-" + str(casa)
    return barrio

def generarCiudad():
    city = random.choice(ciudad)
    return city

def generarTelefono():
    numero = random.randint(1000, 1999)
    return numero

def generarAnoNacimiento():
    numero = random.randint(1930, 2020)
    return numero

def generarProfesion():
    prof = random.choice(profesion)
    return prof

def generarNacionalidad():
    return "Colombia"


#-------------------------Enfermedades y sintomas-----------------------------------

def generarOpcion():
    return random.choice(['Si','No'])

def generarIdEnfermedad():
    id = random.randint(1,9)
    return id

def generarIdSintoma():
    id = random.randint(1,4)
    return id    

def generarFechaRegistro():
    año = random.randint(2019, 2020)
    mes = random.randint(10,12)
    dia = random.randint(10,30)
    texto =""
    texto = str(año) + "-" + str(mes) + "- " + str(dia)
    return texto

def generarTemperatura():
    temperatura = random.randint(34,41)
    return temperatura

 #--------------------------------------LLENAR LA BD-------------------------------------------   

def llenarBD(cantidad):
    i = 0
    while i < cantidad :
        try:
            db = sqlite3.connect("BDD.db")
            cursor = db.cursor()

            documento = generarNumDocumento()
            pac =[documento,
            generarTipoDocumento(),generarNombre(),generarSexo(),generarBarrio(),generarCiudad(),generarTelefono(),
            generarAnoNacimiento(),generarProfesion(),generarNacionalidad()]
            cursor.execute("INSERT INTO Paciente VALUES (?,?,?,?,?,?,?,?,?,?)",pac)



            enf = [documento, generarIdEnfermedad()]
            cursor.execute("INSERT INTO PacienteEnfermedad VALUES (?,?)",enf)

            db.commit() 
            print ("Operacion realizada")
            
            i = i+1

        except sqlite3.OperationalError as errorSQL:
            print("Error ejecutando comando: ",errorSQL)
        finally:
            db.close()
