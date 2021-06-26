#menu juego

#librerías
import tkinter
from tkinter import messagebox

#variables globales
listaconfig=[1, 1, 0, 0, 0, 1]
pila=[]
datos=[]
cont=0
#listaconfig=[dificultad,tiempo,ghoras,gminutos,gsegundos,lado]
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


def validaryjugar(validar,nombre,difi,signof1,signof2,signof3,signof6,signof9,signof10,signof11,signof14,signof17,signof18,signof20,signoc1,signoc2,signoc4,signoc5,signoc8,signoc10,signoc11,signoc13,signoc14,signoc18,signoc19,signoc20,boton1d,boton2d,boton3d,boton4d,boton5d,boton1i,boton2i,boton3i,boton4i,boton5i):

    global listaconfig

    if len(nombre.get())<10 or len(nombre.get())>20:
        messagebox.showerror("Error","El largo del nombre debe estar entre 10 y 20 carácteres")
        return

    if validar.get()==1:
        
        dificultad=listaconfig[0]
        
        if dificultad==1:
            difi.config(text="Nivel - Fácil")
            facil(signof1,signof6,signoc2,signoc4,signoc10,signoc13,signoc14,signoc18,signoc19,signoc20)

        elif dificultado==2:
            difi.config(text="Nivel - Intermedio")
            medio(signof2,signof3,signof11,signof19,signof20,signoc1,signoc5,signoc8,signoc11,signoc19)

        else:
            difi.config(text="Nivel - Difícil")
            dificil(signof9,signof10,signof11,signof14,signof17,signof18,signof19,signoc1,signoc2,signoc4,signoc5,signoc8,signoc19,signoc20)


        lado=listaconfig[5]

        if lado==1:
            derecha(boton1d,boton2d,boton3d,boton4d,boton5d)

        else:
            izquierda(boton1i,boton2i,boton3i,boton4i,boton5i)

    elif validar.get()==0:
        difi.config(text="")
        signof1.config(text="")
        signof2.config(text="")
        signof3.config(text="")
        signof6.config(text="")
        signof9.config(text="")
        signof10.config(text="")
        signof11.config(text="")
        signof14.config(text="")
        signof17.config(text="")
        signof18.config(text="")
        signof20.config(text="")
        signoc1.config(text="")
        signoc2.config(text="")
        signoc4.config(text="")
        signoc5.config(text="")
        signoc8.config(text="")
        signoc10.config(text="")
        signoc11.config(text="")
        signoc13.config(text="")
        signoc14.config(text="")
        signoc18.config(text="")
        signoc19.config(text="")
        signoc20.config(text="")
        boton1d.config(state="disable")
        boton2d.config(state="disable")
        boton3d.config(state="disable")
        boton4d.config(state="disable")
        boton5d.config(state="disable")
        boton1i.config(state="disable")
        boton2i.config(state="disable")
        boton3i.config(state="disable")
        boton4i.config(state="disable")
        boton5i.config(state="disable")        


def borrar():

    global pila
    global datos
    global cont

    if pila==[]:
        messagebox.showerror("Error","No hay jugadas por borrar")
        return

    cont=cont-1
    
    entrada=datos[cont]
    entrada.set("")

    del(pila[-1])


def uno():

    global pila
    global datos
    global cont

    entrada=datos[cont]
    entrada.set("1")
    
    pila=pila+[cont]

    cont=cont+1

    

def dos():

    global pila
    global datos
    global cont

    entrada=datos[cont]
    entrada.set("2")
    
    pila=pila+[cont]

    cont=cont+1


def tres():

    global pila
    global datos
    global cont

    entrada=datos[cont]
    entrada.set("3")
    
    pila=pila+[cont]

    cont=cont+1


def cuatro():

    global pila
    global datos
    global cont

    entrada=datos[cont]
    entrada.set("4")
    
    pila=pila+[cont]

    cont=cont+1


def cinco():

    global pila
    global datos
    global cont

    entrada=datos[cont]
    entrada.set("5")
    
    pila=pila+[cont]

    cont=cont+1




def jugar():
    juego=tkinter.Tk()
    juego.geometry("950x600")
    juego.title("Juego Futoshiki - Jugar")

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
    bvalidar=tkinter.Checkbutton(juego,text="Validar nombre y jugar",variable=validar, onvalue=1, offvalue=0,command=lambda:[validaryjugar(validar,nombre,difi,signof1,signof2,signof3,signof6,signof9,signof10,signof11,signof14,signof17,signof18,signof20,signoc1,signoc2,signoc4,signoc5,signoc8,signoc10,signoc11,signoc13,signoc14,signoc18,signoc19,signoc20,boton1d,boton2d,boton3d,boton4d,boton5d,boton1i,boton2i,boton3i,boton4i,boton5i)])
    bvalidar.grid(row=1,column=3)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=2,column=0)
    
    boton1i=tkinter.Button(juego,text="1",state="disable",height="2",width="5",command=lambda:[uno()])
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

    boton1d=tkinter.Button(juego,text="1",state="disable",height="2",width="5",command=lambda:[uno()])
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

    boton2i=tkinter.Button(juego,text="2",state="disable",height="2",width="5",command=lambda:[dos()])
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

    boton2d=tkinter.Button(juego,text="2",state="disable",height="2",width="5",command=lambda:[dos()])
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

    boton3i=tkinter.Button(juego,text="3",state="disable",height="2",width="5",command=lambda:[tres()])
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

    boton3d=tkinter.Button(juego,text="3",state="disable",height="2",width="5",command=lambda:[tres()])
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

    boton4i=tkinter.Button(juego,text="4",state="disable",height="2",width="5",command=lambda:[cuatro()])
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

    boton4d=tkinter.Button(juego,text="4",state="disable",height="2",width="5",command=lambda:[cuatro()])
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

    boton5i=tkinter.Button(juego,text="5",state="disable",height="2",width="5",command=lambda:[cinco()])
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

    boton5d=tkinter.Button(juego,text="5",state="disable",height="2",width="5",command=lambda:[cinco()])
    boton5d.grid(row=12,column=15)

    blanco=tkinter.Label(juego,text="     ")
    blanco.grid(row=13,column=0)

    iniciarj=tkinter.Button(juego,text="Iniciar\n Juego",bg="red",height="3",width="8")
    iniciarj.grid(row=14,column=5)

    global pila
    pila=[]
    global datos
    datos=[ventrada1,ventrada2,ventrada3,ventrada4,ventrada5,ventrada6,ventrada7,ventrada8,ventrada9,ventrada10,ventrada11,ventrada12,ventrada13,ventrada14,ventrada15,ventrada16,ventrada17,ventrada18,ventrada19,ventrada20,ventrada21,ventrada22,ventrada23,ventrada24,ventrada25]
    
    borrarjugada=tkinter.Button(juego,text="Borrar\n Jugada",bg="cyan",height="3",width="8",command=lambda:[borrar()])
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
                  
jugar()
