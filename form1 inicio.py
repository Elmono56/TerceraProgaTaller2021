#menu inicio

#librerías
import tkinter

#gráficos

def menup():
    inicio=tkinter.Tk()
    inicio.geometry("450x450")
    inicio.title("Juego Futoshiki - Menú de Inicio")

    blanco=tkinter.Label(inicio,text="     ")
    blanco.grid(row=0,column=0)

    irajugar=tkinter.Button(inicio,text="Jugar",height="3",width="11",command=lambda:[inicio.destroy()])
    irajugar.grid(row=1,column=1)

    blanco=tkinter.Label(inicio,text="     ")
    blanco.grid(row=1,column=2)

    configurar=tkinter.Button(inicio,text="Configuración",height="3",width="11",command=lambda:[inicio.destroy()])
    configurar.grid(row=1,column=3)

    blanco=tkinter.Label(inicio,text="     ")
    blanco.grid(row=1,column=4)

    ayuda=tkinter.Button(inicio,text="Ayuda",height="3",width="11",command=lambda:[inicio.destroy()])
    ayuda.grid(row=1,column=5)

    blanco=tkinter.Label(inicio,text="     ")
    blanco.grid(row=1,column=6)

    acercade=tkinter.Button(inicio,text="Acerca de",height="3",width="11",command=lambda:[inicio.destroy()])
    acercade.grid(row=1,column=7)

menup()
