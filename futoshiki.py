#librerías
import tkinter
from tkinter import messagebox
import time
import webbrowser

#variables globales


#gráficos

#gráficos menú de inicio
def menup():
    inicio=tkinter.Tk()
    inicio.geometry("450x450")
    inicio.title("Juego Futoshiki - Menú de Inicio")

    blanco=tkinter.Label(inicio,text="     ")
    blanco.grid(row=0,column=0)

    irajugar=tkinter.Button(inicio,text="Jugar",height="3",width="11",command=lambda:[jugar(),inicio.destroy()])
    irajugar.grid(row=1,column=1)

    blanco=tkinter.Label(inicio,text="     ")
    blanco.grid(row=1,column=2)

    configurar=tkinter.Button(inicio,text="Configuración",height="3",width="11",command=lambda:[configuracion(),inicio.destroy()])
    configurar.grid(row=1,column=3)

    blanco=tkinter.Label(inicio,text="     ")
    blanco.grid(row=1,column=4)

    bayuda=tkinter.Button(inicio,text="Ayuda",height="3",width="11",command=lambda:[ayuda()])
    bayuda.grid(row=1,column=5)

    blanco=tkinter.Label(inicio,text="     ")
    blanco.grid(row=1,column=6)

    bacercade=tkinter.Button(inicio,text="Acerca de",height="3",width="11",command=lambda:[acercade()])
    bacercade.grid(row=1,column=7)


#gráficos menú configuración
def configuracion():
    config=tkinter.Tk()
    config.geometry("700x400")
    config.title("Juego Futoshiki - Configuración")

    blanco=tkinter.Label(config,text="     ")
    blanco.grid(row=0,column=0)

    nivel=tkinter.Label(config,text="1.Nivel: ")
    nivel.grid(row=1,column=1)

    checkfacil=tkinter.IntVar()
    botonfacil=tkinter.Checkbutton(config, text="Fácil   ",variable=checkfacil, onvalue=1, offvalue=0)
    botonfacil.grid(row=2,column=2)

    checkmedio=tkinter.IntVar()
    botonmedio=tkinter.Checkbutton(config, text="Intermedio",variable=checkmedio, onvalue=1, offvalue=0)
    botonmedio.grid(row=3,column=2)

    checkdificil=tkinter.IntVar()
    botondificil=tkinter.Checkbutton(config, text="Difícil  ",variable=checkdificil, onvalue=1, offvalue=0)
    botondificil.grid(row=4,column=2)

    blanco=tkinter.Label(config,text="     ")
    blanco.grid(row=0,column=3)

    reloj=tkinter.Label(config,text="2.Tiempo: ")
    reloj.grid(row=1,column=4)

    checktiemposi=tkinter.IntVar()
    botonrsi=tkinter.Checkbutton(config, text="Sí     ",variable=checktiemposi, onvalue=1, offvalue=0)
    botonrsi.grid(row=2,column=5)

    checktiempono=tkinter.IntVar()
    botonrno=tkinter.Checkbutton(config, text="No      ",variable=checktiempono, onvalue=1, offvalue=0)
    botonrno.grid(row=3,column=5)

    checktimer=tkinter.IntVar()
    botonrtimer=tkinter.Checkbutton(config, text="Timer",variable=checktimer, onvalue=1, offvalue=0,command=lambda:[activarhms(checktimer,entradah,entradam,entradas)])
    botonrtimer.grid(row=4,column=5)

    horas=tkinter.Label(config,text="Horas")
    horas.grid(row=5,column=4)

    entradah=tkinter.Entry(config,width="5",state="disable")
    entradah.grid(row=6,column=4)

    minutos=tkinter.Label(config,text="Minutos")
    minutos.grid(row=5,column=5)

    entradam=tkinter.Entry(config,width="5",state="disable")
    entradam.grid(row=6,column=5)

    segundos=tkinter.Label(config,text="Segundos")
    segundos.grid(row=5,column=6)

    entradas=tkinter.Entry(config,width="5",state="disable")
    entradas.grid(row=6,column=6)

    blanco=tkinter.Label(config,text="     ")
    blanco.grid(row=0,column=7)

    posicion=tkinter.Label(config,text="3.Posición del panel de dígitos: ")
    posicion.grid(row=1,column=8)

    checkderecha=tkinter.IntVar()
    pderecha=tkinter.Checkbutton(config,text="Derecha",variable=checkderecha, onvalue=1, offvalue=0)
    pderecha.grid(row=2,column=9)

    checkizquierda=tkinter.IntVar()
    pizquierda=tkinter.Checkbutton(config,text="Izquierda",variable=checkizquierda, onvalue=1, offvalue=0)
    pizquierda.grid(row=3,column=9)

    blanco=tkinter.Label(config,text="     ")
    blanco.grid(row=7,column=0)

    guardarc=tkinter.Button(config,text="Guardar configuración",height="2",width="20",command=lambda:[guardarconfig(checkfacil,checkmedio,checkdificil,checktiemposi,checktiempono,checktimer,entradah,entradam,entradas,checkderecha,checkizquierda)])
    guardarc.grid(row=8,column=8)


#gráficos menú de juego
def jugar():
    juego=tkinter.Tk()
    juego.geometry("950x600")
    juego.title("Juego Futoshiki - Jugar")

    global pila
    pila=[]
    global cont
    cont=0
    
    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=0,column=0)

    futo=tkinter.Label(juego,text="FUTOSHIKI",bg="red")
    futo.grid(row=0,column=9)

    difi=tkinter.Label(juego,text="")
    difi.grid(row=1,column=9)

    diginombre=tkinter.Label(juego,text="Nombre del jugador:")
    diginombre.grid(row=1,column=1)

    nombre=tkinter.Entry(juego)
    nombre.grid(row=1,column=2)

    validar=tkinter.IntVar()
    bvalidar=tkinter.Checkbutton(juego,text="Validar nombre y jugar",variable=validar, onvalue=1, offvalue=0,command=lambda:[validaryjugar(validar,nombre,difi,iniciarj,cargarj)])
    bvalidar.grid(row=1,column=3)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=2,column=0)
    
    boton1i=tkinter.Button(juego,text="1",state="disable",height="2",width="5",command=lambda:[agregar("1")])
    boton1i.grid(row=4,column=3)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=4,column=4)

    ventrada1=tkinter.StringVar()
    ventrada1.set("")
    entrada1=tkinter.Entry(juego,textvariable=ventrada1,state="disable",width="6")
    entrada1.grid(row=4,column=5)

    signof1=tkinter.Label(juego,text="")
    signof1.grid(row=4,column=6)

    ventrada2=tkinter.StringVar()
    ventrada2.set("")
    entrada2=tkinter.Entry(juego,textvariable=ventrada2,state="disable",width="6")
    entrada2.grid(row=4,column=7)

    signof2=tkinter.Label(juego,text="")
    signof2.grid(row=4,column=8)

    ventrada3=tkinter.StringVar()
    ventrada3.set("")
    entrada3=tkinter.Entry(juego,textvariable=ventrada3,state="disable",width="6")
    entrada3.grid(row=4,column=9)

    signof3=tkinter.Label(juego,text="")
    signof3.grid(row=4,column=10)

    ventrada4=tkinter.StringVar()
    ventrada4.set("")
    entrada4=tkinter.Entry(juego,textvariable=ventrada4,state="disable",width="6")
    entrada4.grid(row=4,column=11)

    signof4=tkinter.Label(juego,text="")
    signof4.grid(row=4,column=12)

    ventrada5=tkinter.StringVar()
    ventrada5.set("")
    entrada5=tkinter.Entry(juego,textvariable=ventrada5,state="disable",width="6")
    entrada5.grid(row=4,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=4,column=14)

    boton1d=tkinter.Button(juego,text="1",state="disable",height="2",width="5",command=lambda:[agregar("1")])
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

    boton2i=tkinter.Button(juego,text="2",state="disable",height="2",width="5",command=lambda:[agregar("2")])
    boton2i.grid(row=6,column=3)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=6,column=4)

    ventrada6=tkinter.StringVar()
    ventrada6.set("")
    entrada6=tkinter.Entry(juego,textvariable=ventrada6,state="disable",width="6")
    entrada6.grid(row=6,column=5)

    signof5=tkinter.Label(juego,text="")
    signof5.grid(row=6,column=6)

    ventrada7=tkinter.StringVar()
    ventrada7.set("")
    entrada7=tkinter.Entry(juego,textvariable=ventrada7,state="disable",width="6")
    entrada7.grid(row=6,column=7)

    signof6=tkinter.Label(juego,text="")
    signof6.grid(row=6,column=8)

    ventrada8=tkinter.StringVar()
    ventrada8.set("")
    entrada8=tkinter.Entry(juego,textvariable=ventrada8,state="disable",width="6")
    entrada8.grid(row=6,column=9)

    signof7=tkinter.Label(juego,text="")
    signof7.grid(row=6,column=10)

    ventrada9=tkinter.StringVar()
    ventrada9.set("")
    entrada9=tkinter.Entry(juego,textvariable=ventrada9,state="disable",width="6")
    entrada9.grid(row=6,column=11)

    signof8=tkinter.Label(juego,text="")
    signof8.grid(row=6,column=12)

    ventrada10=tkinter.StringVar()
    ventrada10.set("")
    entrada10=tkinter.Entry(juego,textvariable=ventrada10,state="disable",width="6")
    entrada10.grid(row=6,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=6,column=14)

    boton2d=tkinter.Button(juego,text="2",state="disable",height="2",width="5",command=lambda:[agregar("2")])
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

    boton3i=tkinter.Button(juego,text="3",state="disable",height="2",width="5",command=lambda:[agregar("3")])
    boton3i.grid(row=8,column=3)

    ventrada11=tkinter.StringVar()
    ventrada11.set("")
    entrada11=tkinter.Entry(juego,textvariable=ventrada11,state="disable",width="6")
    entrada11.grid(row=8,column=5)

    signof9=tkinter.Label(juego,text="")
    signof9.grid(row=8,column=6)

    ventrada12=tkinter.StringVar()
    ventrada12.set("")
    entrada12=tkinter.Entry(juego,textvariable=ventrada12,state="disable",width="6")
    entrada12.grid(row=8,column=7)

    signof10=tkinter.Label(juego,text="")
    signof10.grid(row=8,column=8)

    ventrada13=tkinter.StringVar()
    ventrada13.set("")
    entrada13=tkinter.Entry(juego,textvariable=ventrada13,state="disable",width="6")
    entrada13.grid(row=8,column=9)

    signof11=tkinter.Label(juego,text="")
    signof11.grid(row=8,column=10)

    ventrada14=tkinter.StringVar()
    ventrada14.set("")
    entrada14=tkinter.Entry(juego,textvariable=ventrada14,state="disable",width="6")
    entrada14.grid(row=8,column=11)

    signof12=tkinter.Label(juego,text="")
    signof12.grid(row=8,column=12)

    ventrada15=tkinter.StringVar()
    ventrada15.set("")
    entrada15=tkinter.Entry(juego,textvariable=ventrada15,state="disable",width="6")
    entrada15.grid(row=8,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=8,column=14)

    boton3d=tkinter.Button(juego,text="3",state="disable",height="2",width="5",command=lambda:[agregar("3")])
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

    boton4i=tkinter.Button(juego,text="4",state="disable",height="2",width="5",command=lambda:[agregar("4")])
    boton4i.grid(row=10,column=3)

    ventrada16=tkinter.StringVar()
    ventrada16.set("")
    entrada16=tkinter.Entry(juego,textvariable=ventrada16,state="disable",width="6")
    entrada16.grid(row=10,column=5)

    signof13=tkinter.Label(juego,text="")
    signof13.grid(row=10,column=6)

    ventrada17=tkinter.StringVar()
    ventrada17.set("")
    entrada17=tkinter.Entry(juego,textvariable=ventrada17,state="disable",width="6")
    entrada17.grid(row=10,column=7)

    signof14=tkinter.Label(juego,text="")
    signof14.grid(row=10,column=8)

    ventrada18=tkinter.StringVar()
    ventrada18.set("")
    entrada18=tkinter.Entry(juego,textvariable=ventrada18,state="disable",width="6")
    entrada18.grid(row=10,column=9)

    signof15=tkinter.Label(juego,text="")
    signof15.grid(row=10,column=10)

    ventrada19=tkinter.StringVar()
    ventrada19.set("")
    entrada19=tkinter.Entry(juego,textvariable=ventrada19,state="disable",width="6")
    entrada19.grid(row=10,column=11)

    signof16=tkinter.Label(juego,text="")
    signof16.grid(row=10,column=12)

    ventrada20=tkinter.StringVar()
    ventrada20.set("")
    entrada20=tkinter.Entry(juego,textvariable=ventrada20,state="disable",width="6")
    entrada20.grid(row=10,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=10,column=14)

    boton4d=tkinter.Button(juego,text="4",state="disable",height="2",width="5",command=lambda:[agregar("4")])
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

    boton5i=tkinter.Button(juego,text="5",state="disable",height="2",width="5",command=lambda:[agregar("5")])
    boton5i.grid(row=12,column=3)

    ventrada21=tkinter.StringVar()
    ventrada21.set("")
    entrada21=tkinter.Entry(juego,textvariable=ventrada21,state="disable",width="6")
    entrada21.grid(row=12,column=5)

    signof17=tkinter.Label(juego,text="")
    signof17.grid(row=12,column=6)

    ventrada22=tkinter.StringVar()
    ventrada22.set("")
    entrada22=tkinter.Entry(juego,textvariable=ventrada22,state="disable",width="6")
    entrada22.grid(row=12,column=7)

    signof18=tkinter.Label(juego,text="")
    signof18.grid(row=12,column=8)

    ventrada23=tkinter.StringVar()
    ventrada23.set("")
    entrada23=tkinter.Entry(juego,textvariable=ventrada23,state="disable",width="6")
    entrada23.grid(row=12,column=9)

    signof19=tkinter.Label(juego,text="")
    signof19.grid(row=12,column=10)

    ventrada24=tkinter.StringVar()
    ventrada24.set("")
    entrada24=tkinter.Entry(juego,textvariable=ventrada24,state="disable",width="6")
    entrada24.grid(row=12,column=11)

    signof20=tkinter.Label(juego,text="")
    signof20.grid(row=12,column=12)

    ventrada25=tkinter.StringVar()
    ventrada25.set("")
    entrada25=tkinter.Entry(juego,textvariable=ventrada25,state="disable",width="6")
    entrada25.grid(row=12,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=12,column=14)

    boton5d=tkinter.Button(juego,text="5",state="disable",height="2",width="5",command=lambda:[agregar("5")])
    boton5d.grid(row=12,column=15)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=13,column=0)

    iniciarj=tkinter.Button(juego,text="Iniciar\n Juego",state="disable",bg="red",height="3",width="8",command=lambda:[iniciar(boton1d,boton2d,boton3d,boton4d,boton5d,boton1i,boton2i,boton3i,boton4i,boton5i,nombre,bvalidar,borrarjugada,terminarj,borrarjuego,guardarj,signof1,signof2,signof3,signof6,signof9,signof10,signof11,signof14,signof17,signof18,signof19,signof20,signoc1,signoc2,signoc4,signoc5,signoc8,signoc10,signoc11,signoc13,signoc14,signoc18,signoc19,signoc20,iniciarj,cargarj),temporizador(h,m,s,juego)])
    iniciarj.grid(row=14,column=5)

    global datos
    datos=[ventrada1,ventrada2,ventrada3,ventrada4,ventrada5,ventrada6,ventrada7,ventrada8,ventrada9,ventrada10,ventrada11,ventrada12,ventrada13,ventrada14,ventrada15,ventrada16,ventrada17,ventrada18,ventrada19,ventrada20,ventrada21,ventrada22,ventrada23,ventrada24,ventrada25]
    
    borrarjugada=tkinter.Button(juego,text="Borrar\n Jugada",state="disable",bg="cyan",height="3",width="8",command=lambda:[fborrarjugada()])
    borrarjugada.grid(row=14,column=7)

    terminarj=tkinter.Button(juego,text="Terminar\n Juego",state="disable",bg="light green",height="3",width="8",command=lambda:[terminarjuego(juego)])
    terminarj.grid(row=14,column=9)

    borrarjuego=tkinter.Button(juego,text="Borrar\n Juego",state="disable",bg="light blue",height="3",width="8",command=lambda:[fborrarjuego(ventrada1,ventrada2,ventrada3,ventrada4,ventrada5,ventrada6,ventrada7,ventrada8,ventrada9,ventrada10,ventrada11,ventrada12,ventrada13,ventrada14,ventrada15,ventrada16,ventrada17,ventrada18,ventrada19,ventrada20,ventrada21,ventrada22,ventrada23,ventrada24,ventrada25)])
    borrarjuego.grid(row=14,column=11)

    top10=tkinter.Button(juego,text="Top\n 10",bg="yellow",height="3",width="7")
    top10.grid(row=14,column=13)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=15,column=0)

    lhoras=tkinter.Label(juego,text="Horas")
    lhoras.grid(row=16,column=1)

    lminutos=tkinter.Label(juego,text="Minutos")
    lminutos.grid(row=16,column=2)

    lsegundos=tkinter.Label(juego,text="Segundos")
    lsegundos.grid(row=16,column=3)

    h=tkinter.Label(juego,text=00)
    h.grid(row=17,column=1)

    m=tkinter.Label(juego,text=00)
    m.grid(row=17,column=2)

    s=tkinter.Label(juego,text=00)
    s.grid(row=17,column=3)

    guardarj=tkinter.Button(juego,text="Guardar Juego",state="disable",height="2",width="11")
    guardarj.grid(row=17,column=9)

    cargarj=tkinter.Button(juego,text="Cargar Juego",state="disable",height="2",width="11")
    cargarj.grid(row=17,column=11)


#Acerca de
def acercade():
    messagebox.showinfo("Acerca del programa","Juego Futoshiki\n Versión: 1.4.3\n Fecha de creación: 15-06-2021\n Desarrollador: Jose Pablo Hidalgo Navarro")

#Ayuda
def ayuda():
    archivo="manual_de_usuario_futoshiki.pdf"
    webbrowser.open_new(archivo)

#funciones auxiliares






menup()
