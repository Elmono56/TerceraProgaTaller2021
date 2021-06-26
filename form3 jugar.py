#menu juego

#librerías
import tkinter
from tkinter import messagebox

#funciones aux

#gráficos

def facil(signof1,signof6,signoc2,signoc4,signoc10,signoc13,signoc14,signoc18,signoc19,signoc20):
    
    signof1.config(text="<")
    signof6.config(text="<")
    signoc2.config(text="^")
    signoc4.config(text="^")
    signoc10.config(text="v")
    signoc13.config(text="v")
    signoc14.config(text="^")
    signoc18.config(text="v")
    signoc19.config(text="v")
    signoc20.config(text="^")
    

def medio(signof2,signof3,signof11,signof19,signof20,signoc1,signoc5,signoc8,signoc11,signoc19):

    signof2.config(text="<")
    signof3.config(text="<")
    signof11.config(text=">")
    signof19.config(text=">")
    signof20.config(text="<")
    signoc1.config(text="^")
    signoc5.config(text="^")
    signoc8.config(text="v")
    signoc11.config(text="v")
    signoc19.config(text="^")


def dificil(signof9,signof10,signof11,signof14,signof17,signof18,signof19,signoc1,signoc2,signoc4,signoc5,signoc8,signoc19,signoc20):
    
    signof9.config(text=">")
    signof10.config(text=">")
    signof11.config(text="<")
    signof14.config(text="<")
    signof17.config(text="<")
    signof18.config(text="<")
    signof19.config(text=">")
    signoc1.config(text="v")
    signoc2.config(text="^")
    signoc4.config(text="^")
    signoc5.config(text="^")
    signoc8.config(text="^")
    signoc19.config(text="v")
    signoc20.config(text="^")


def derecha(boton1d,boton2d,boton3d,boton4d,boton5d):
    
    boton1d.config(state="normal")
    boton2d.config(state="normal")
    boton3d.config(state="normal")
    boton4d.config(state="normal")
    boton5d.config(state="normal")

def izquierda(boton1i,boton2i,boton3i,boton4i,boton5i):
    
    boton1i.config(state="normal")
    boton2i.config(state="normal")
    boton3i.config(state="normal")
    boton4i.config(state="normal")
    boton5i.config(state="normal")



def jugar():
    juego=tkinter.Tk()
    juego.geometry("900x600")
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
    
    boton1i=tkinter.Button(juego,text="1",state="disable",height="2",width="5")
    boton1i.grid(row=4,column=3)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=4,column=4)

    entrada1=tkinter.Entry(juego,width="6")
    entrada1.grid(row=4,column=5)

    signof1=tkinter.Label(juego,text="")
    signof1.grid(row=4,column=6)

    entrada2=tkinter.Entry(juego,width="6")
    entrada2.grid(row=4,column=7)

    signof2=tkinter.Label(juego,text="")
    signof2.grid(row=4,column=8)

    entrada3=tkinter.Entry(juego,width="6")
    entrada3.grid(row=4,column=9)

    signof3=tkinter.Label(juego,text="")
    signof3.grid(row=4,column=10)

    entrada4=tkinter.Entry(juego,width="6")
    entrada4.grid(row=4,column=11)

    signof4=tkinter.Label(juego,text="")
    signof4.grid(row=4,column=12)

    entrada5=tkinter.Entry(juego,width="6")
    entrada5.grid(row=4,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=4,column=14)

    boton1d=tkinter.Button(juego,text="1",state="disable",height="2",width="5")
    boton1d.grid(row=4,column=15)

    signoc1=tkinter.Label(juego,text="")
    signoc1.grid(row=5,column=5)

    signoc2=tkinter.Label(juego,text="")
    signoc2.grid(row=5,column=7)

    signoc3=tkinter.Label(juego,text="")
    signoc3.grid(row=5,column=9)

    signoc4=tkinter.Label(juego,text="")
    signoc4.grid(row=5,column=11)

    signoc5=tkinter.Label(juego,text="")
    signoc5.grid(row=5,column=13)

    boton2i=tkinter.Button(juego,text="2",state="disable",height="2",width="5")
    boton2i.grid(row=6,column=3)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=6,column=4)

    entrada6=tkinter.Entry(juego,width="6")
    entrada6.grid(row=6,column=5)

    signof5=tkinter.Label(juego,text="")
    signof5.grid(row=6,column=6)

    entrada7=tkinter.Entry(juego,width="6")
    entrada7.grid(row=6,column=7)

    signof6=tkinter.Label(juego,text="")
    signof6.grid(row=6,column=8)

    entrada8=tkinter.Entry(juego,width="6")
    entrada8.grid(row=6,column=9)

    signof7=tkinter.Label(juego,text="")
    signof7.grid(row=6,column=10)

    entrada9=tkinter.Entry(juego,width="6")
    entrada9.grid(row=6,column=11)

    signof8=tkinter.Label(juego,text="")
    signof8.grid(row=6,column=12)

    entrada10=tkinter.Entry(juego,width="6")
    entrada10.grid(row=6,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=6,column=14)

    boton2d=tkinter.Button(juego,text="2",state="disable",height="2",width="5")
    boton2d.grid(row=6,column=15)

    signoc6=tkinter.Label(juego,text="")
    signoc6.grid(row=7,column=5)

    signoc7=tkinter.Label(juego,text="")
    signoc7.grid(row=7,column=7)

    signoc8=tkinter.Label(juego,text="")
    signoc8.grid(row=7,column=9)

    signoc9=tkinter.Label(juego,text="")
    signoc9.grid(row=7,column=11)

    signoc10=tkinter.Label(juego,text="")
    signoc10.grid(row=7,column=13)

    boton3i=tkinter.Button(juego,text="3",state="disable",height="2",width="5")
    boton3i.grid(row=8,column=3)

    entrada11=tkinter.Entry(juego,width="6")
    entrada11.grid(row=8,column=5)

    signof9=tkinter.Label(juego,text="")
    signof9.grid(row=8,column=6)

    entrada12=tkinter.Entry(juego,width="6")
    entrada12.grid(row=8,column=7)

    signof10=tkinter.Label(juego,text="")
    signof10.grid(row=8,column=8)

    entrada13=tkinter.Entry(juego,width="6")
    entrada13.grid(row=8,column=9)

    signof11=tkinter.Label(juego,text="")
    signof11.grid(row=8,column=10)

    entrada14=tkinter.Entry(juego,width="6")
    entrada14.grid(row=8,column=11)

    signof12=tkinter.Label(juego,text="")
    signof12.grid(row=8,column=12)

    entrada15=tkinter.Entry(juego,width="6")
    entrada15.grid(row=8,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=8,column=14)

    boton3d=tkinter.Button(juego,text="3",state="disable",height="2",width="5")
    boton3d.grid(row=8,column=15)

    signoc11=tkinter.Label(juego,text="")
    signoc11.grid(row=9,column=5)

    signoc12=tkinter.Label(juego,text="")
    signoc12.grid(row=9,column=7)

    signoc13=tkinter.Label(juego,text="")
    signoc13.grid(row=9,column=9)

    signoc14=tkinter.Label(juego,text="")
    signoc14.grid(row=9,column=11)

    signoc15=tkinter.Label(juego,text="")
    signoc15.grid(row=9,column=13)

    boton4i=tkinter.Button(juego,text="4",state="disable",height="2",width="5")
    boton4i.grid(row=10,column=3)

    entrada16=tkinter.Entry(juego,width="6")
    entrada16.grid(row=10,column=5)

    signof13=tkinter.Label(juego,text="")
    signof13.grid(row=10,column=6)

    entrada17=tkinter.Entry(juego,width="6")
    entrada17.grid(row=10,column=7)

    signof14=tkinter.Label(juego,text="")
    signof14.grid(row=10,column=8)

    entrada18=tkinter.Entry(juego,width="6")
    entrada18.grid(row=10,column=9)

    signof15=tkinter.Label(juego,text="")
    signof15.grid(row=10,column=10)

    entrada19=tkinter.Entry(juego,width="6")
    entrada19.grid(row=10,column=11)

    signof16=tkinter.Label(juego,text="")
    signof16.grid(row=10,column=12)

    entrada20=tkinter.Entry(juego,width="6")
    entrada20.grid(row=10,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=10,column=14)

    boton4d=tkinter.Button(juego,text="4",state="disable",height="2",width="5")
    boton4d.grid(row=10,column=15)

    signoc16=tkinter.Label(juego,text="")
    signoc16.grid(row=11,column=5)

    signoc17=tkinter.Label(juego,text="")
    signoc17.grid(row=11,column=7)

    signoc18=tkinter.Label(juego,text="")
    signoc18.grid(row=11,column=9)

    signoc19=tkinter.Label(juego,text="")
    signoc19.grid(row=11,column=11)

    signoc20=tkinter.Label(juego,text="")
    signoc20.grid(row=11,column=13)

    boton5i=tkinter.Button(juego,text="5",state="disable",height="2",width="5")
    boton5i.grid(row=12,column=3)

    entrada21=tkinter.Entry(juego,width="6")
    entrada21.grid(row=12,column=5)

    signof17=tkinter.Label(juego,text="")
    signof17.grid(row=12,column=6)

    entrada22=tkinter.Entry(juego,width="6")
    entrada22.grid(row=12,column=7)

    signof18=tkinter.Label(juego,text="")
    signof18.grid(row=12,column=8)

    entrada23=tkinter.Entry(juego,width="6")
    entrada23.grid(row=12,column=9)

    signof19=tkinter.Label(juego,text="")
    signof19.grid(row=12,column=10)

    entrada24=tkinter.Entry(juego,width="6")
    entrada24.grid(row=12,column=11)

    signof20=tkinter.Label(juego,text="")
    signof20.grid(row=12,column=12)

    entrada25=tkinter.Entry(juego,width="6")
    entrada25.grid(row=12,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=12,column=14)

    boton5d=tkinter.Button(juego,text="5",state="disable",height="2",width="5")
    boton5d.grid(row=12,column=15)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=13,column=0)

    iniciarj=tkinter.Button(juego,text="Iniciar\n Juego",bg="red",height="3",width="8")
    iniciarj.grid(row=14,column=5)

    borrarjugada=tkinter.Button(juego,text="Borrar\n Jugada",bg="cyan",height="3",width="8")
    borrarjugada.grid(row=14,column=7)

    terminarj=tkinter.Button(juego,text="Terminar\n Juego",bg="green",height="3",width="8")
    terminarj.grid(row=14,column=9)

    borrarjuego=tkinter.Button(juego,text="Borrar\n Juego",bg="light blue",height="3",width="8")
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

    guardarj=tkinter.Button(juego,text="Guardar Juego",height="2",width="11")
    guardarj.grid(row=17,column=9)

    cargarj=tkinter.Button(juego,text="Cargar Juego",height="2",width="11")
    cargarj.grid(row=17,column=11)

    #facil(signof1,signof6,signoc2,signoc4,signoc10,signoc13,signoc14,signoc18,signoc19,signoc20)
    #medio(signof2,signof3,signof11,signof19,signof20,signoc1,signoc5,signoc8,signoc11,
    #dificil(signof9,signof10,signof11,signof14,signof17,signof18,signof19,signoc1,signoc2,signoc4,signoc5,signoc8,signoc19,signoc20)
    #derecha(boton1d,boton2d,boton3d,boton4d,boton5d)
    izquierda(boton1i,boton2i,boton3i,boton4i,boton5i)
                  
jugar()
