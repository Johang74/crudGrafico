#Johan David Gomez Gil
#Lenguajes 2 
#2020

#from generador import *
from vista import *
from tkinter import Tk,mainloop


def prueba():
    print ('Principal')
    #llenarBD(5)

def interfaz():
    interfaz = Tk()
    crud = ventana(interfaz)
    interfaz.mainloop()



if __name__ == '__main__':
    #prueba()
    interfaz()
