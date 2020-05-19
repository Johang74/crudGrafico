#Johan David Gomez Gil
#Sebastian Bustamante
#Lenguajes 2 
#2020


import sqlite3


class Datos:

    database = 'BDD.db'

    #def __init__(self, consulta, parametros =()):
        #self.consulta = consulta
        #self.parametros = parametros


    def ejecutarConsulta(self,consulta, parametros = ()):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            resultados = cursor.execute(consulta, parametros)
            conn.commit()
        return resultados