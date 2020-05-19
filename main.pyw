#Johan David Gomez Gil
#Sebastian Bustamante
#Lenguajes 2 
#2020

#from generador import *
from vista import *
from tkinter import Tk,mainloop



def interfaz():
    interfaz = Tk()
    crud = ventana(interfaz)
    interfaz.mainloop()



if __name__ == '__main__':
    interfaz()

