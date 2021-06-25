#menu juego

#librerías
import tkinter
from tkinter import messagebox

#funciones aux

#gráficos

def jugar():
    juego=tkinter.Tk()
    juego.geometry("1000x700")
    juego.title("Juego Futoshiki - Jugar")

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=0,column=0)

    futo=tkinter.Label(juego,text="FUTOSHIKI",bg="red")
    futo.grid(row=0,column=9)

    difi=tkinter.Label(juego,text="Dificultad fácil")
    difi.grid(row=1,column=9)

    diginombre=tkinter.Label(juego,text="Nombre del jugador:")
    diginombre.grid(row=1,column=1)

    nombre=tkinter.Entry(juego)
    nombre.grid(row=1,column=2)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=2,column=0)
    
    boton1d=tkinter.Button(juego,text="1",height="2",width="5")
    boton1d.grid(row=4,column=3)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=4,column=4)

    entrada1=tkinter.Entry(juego,width="5")
    entrada1.grid(row=4,column=5)

    signo1=tkinter.Label(juego,text="<")
    signo1.grid(row=4,column=6)

    entrada2=tkinter.Entry(juego,width="5")
    entrada2.grid(row=4,column=7)

    signo2=tkinter.Label(juego,text="<")
    signo2.grid(row=4,column=8)

    entrada3=tkinter.Entry(juego,width="5")
    entrada3.grid(row=4,column=9)

    signo3=tkinter.Label(juego,text="<")
    signo3.grid(row=4,column=10)

    entrada4=tkinter.Entry(juego,width="5")
    entrada4.grid(row=4,column=11)

    signo4=tkinter.Label(juego,text="<")
    signo4.grid(row=4,column=12)

    entrada5=tkinter.Entry(juego,width="5")
    entrada5.grid(row=4,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=4,column=14)

    boton1i=tkinter.Button(juego,text="1",height="2",width="5")
    boton1i.grid(row=4,column=15)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=5,column=0)

    boton2d=tkinter.Button(juego,text="2",height="2",width="5")
    boton2d.grid(row=6,column=3)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=6,column=4)

    entrada6=tkinter.Entry(juego,width="5")
    entrada6.grid(row=6,column=5)

    signo5=tkinter.Label(juego,text="<")
    signo5.grid(row=6,column=6)

    entrada7=tkinter.Entry(juego,width="5")
    entrada7.grid(row=6,column=7)

    signo6=tkinter.Label(juego,text="<")
    signo6.grid(row=6,column=8)

    entrada8=tkinter.Entry(juego,width="5")
    entrada8.grid(row=6,column=9)

    signo7=tkinter.Label(juego,text="<")
    signo7.grid(row=6,column=10)

    entrada9=tkinter.Entry(juego,width="5")
    entrada9.grid(row=6,column=11)

    signo8=tkinter.Label(juego,text="<")
    signo8.grid(row=6,column=12)

    entrada10=tkinter.Entry(juego,width="5")
    entrada10.grid(row=6,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=6,column=14)

    boton2i=tkinter.Button(juego,text="2",height="2",width="5")
    boton2i.grid(row=6,column=15)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=7,column=4)

    boton3d=tkinter.Button(juego,text="3",height="2",width="5")
    boton3d.grid(row=8,column=3)

    entrada11=tkinter.Entry(juego,width="5")
    entrada11.grid(row=8,column=5)

    signo9=tkinter.Label(juego,text="<")
    signo9.grid(row=8,column=6)

    entrada12=tkinter.Entry(juego,width="5")
    entrada12.grid(row=8,column=7)

    signo10=tkinter.Label(juego,text="<")
    signo10.grid(row=8,column=8)

    entrada13=tkinter.Entry(juego,width="5")
    entrada13.grid(row=8,column=9)

    signo11=tkinter.Label(juego,text="<")
    signo11.grid(row=8,column=10)

    entrada14=tkinter.Entry(juego,width="5")
    entrada14.grid(row=8,column=11)

    signo12=tkinter.Label(juego,text="<")
    signo12.grid(row=8,column=12)

    entrada15=tkinter.Entry(juego,width="5")
    entrada15.grid(row=8,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=8,column=14)

    boton3i=tkinter.Button(juego,text="3",height="2",width="5")
    boton3i.grid(row=8,column=15)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=9,column=4)

    boton4d=tkinter.Button(juego,text="4",height="2",width="5")
    boton4d.grid(row=10,column=3)

    entrada16=tkinter.Entry(juego,width="5")
    entrada16.grid(row=10,column=5)

    signo13=tkinter.Label(juego,text="<")
    signo13.grid(row=10,column=6)

    entrada17=tkinter.Entry(juego,width="5")
    entrada17.grid(row=10,column=7)

    signo14=tkinter.Label(juego,text="<")
    signo14.grid(row=10,column=8)

    entrada18=tkinter.Entry(juego,width="5")
    entrada18.grid(row=10,column=9)

    signo15=tkinter.Label(juego,text="<")
    signo15.grid(row=10,column=10)

    entrada19=tkinter.Entry(juego,width="5")
    entrada19.grid(row=10,column=11)

    signo16=tkinter.Label(juego,text="<")
    signo16.grid(row=10,column=12)

    entrada20=tkinter.Entry(juego,width="5")
    entrada20.grid(row=10,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=10,column=14)

    boton4i=tkinter.Button(juego,text="4",height="2",width="5")
    boton4i.grid(row=10,column=15)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=11,column=4)

    boton5d=tkinter.Button(juego,text="5",height="2",width="5")
    boton5d.grid(row=12,column=3)

    entrada21=tkinter.Entry(juego,width="5")
    entrada21.grid(row=12,column=5)

    signo17=tkinter.Label(juego,text="<")
    signo17.grid(row=12,column=6)

    entrada22=tkinter.Entry(juego,width="5")
    entrada22.grid(row=12,column=7)

    signo18=tkinter.Label(juego,text="<")
    signo18.grid(row=12,column=8)

    entrada23=tkinter.Entry(juego,width="5")
    entrada23.grid(row=12,column=9)

    signo19=tkinter.Label(juego,text="<")
    signo19.grid(row=12,column=10)

    entrada24=tkinter.Entry(juego,width="5")
    entrada24.grid(row=12,column=11)

    signo20=tkinter.Label(juego,text="<")
    signo20.grid(row=12,column=12)

    entrada25=tkinter.Entry(juego,width="5")
    entrada25.grid(row=12,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=12,column=14)

    boton5i=tkinter.Button(juego,text="5",height="2",width="5")
    boton5i.grid(row=12,column=15)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=13,column=0)

    iniciarj=tkinter.Button(juego,text="Iniciar\n Juego",bg="red",height="3",width="7")
    iniciarj.grid(row=14,column=5)

    borrarjugada=tkinter.Button(juego,text="Borrar\n Jugada",bg="cyan",height="3",width="7")
    borrarjugada.grid(row=14,column=7)

    terminarj=tkinter.Button(juego,text="Terminar\n Juego",bg="green",height="3",width="7")
    terminarj.grid(row=14,column=9)

    borrarjuego=tkinter.Button(juego,text="Borrar\n Juego",bg="light blue",height="3",width="7")
    borrarjuego.grid(row=14,column=11)

    top10=tkinter.Button(juego,text="Top\n 10",bg="yellow",height="3",width="7")
    top10.grid(row=14,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=15,column=0)

    horas=tkinter.Label(juego,text="Horas")
    horas.grid(row=16,column=1)

    minutos=tkinter.Label(juego,text="Minutos")
    minutos.grid(row=16,column=2)

    segundos=tkinter.Label(juego,text="Segundos")
    segundos.grid(row=16,column=3)

    h=tkinter.Label(juego,text=00)
    h.grid(row=17,column=1)

    m=tkinter.Label(juego,text=00)
    m.grid(row=17,column=2)

    s=tkinter.Label(juego,text=00)
    s.grid(row=17,column=3)

    guardarj=tkinter.Button(juego,text="Guardar Juego",height="2",width="10")
    guardarj.grid(row=17,column=9)

    cargarj=tkinter.Button(juego,text="Cargar Juego",height="2",width="10")
    cargarj.grid(row=17,column=11)




                  
jugar()
