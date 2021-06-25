#menu configuracion

#librerías
import tkinter
from tkinter import messagebox

#funciones aux
def activarhms(checktimer,entradah,entradam,entradas):
    if checktimer.get() == 1:
        entradah['state'] = "normal"
        entradam['state'] = "normal"
        entradas['state'] = "normal"
    elif checktimer.get() == 0:
        entradah['state'] = "disable"
        entradam['state'] = "disable"
        entradas['state'] = "disable"

def guardarconfig(checkfacil,checkmedio,checkdificil,checktiemposi,checktiempono,checktimer,entradah,entradam,entradas,checkderecha,checkizquierda):

    gfacil=checkfacil.get()
    gmedio=checkmedio.get()
    gdificil=checkdificil.get()
    totalnivel=gfacil+gmedio+gdificil

    if totalnivel==0:
        messagebox.showerror("Error","Debe seleccionar una casilla en nivel")
        return
    elif totalnivel>1:
        messagebox.showerror("Error","Debe seleccionar solo una casilla en nivel")
        return

    if gfacil==1:
        dificultad=1
    if gmedio==1:
        dificultad=2
    if gdificil==1:
        dificultad=3
        
    gtsi=checktiemposi.get()
    gtno=checktiempono.get()
    gttimer=checktimer.get()
    totaltiempo=gtsi+gtno+gttimer

    if totaltiempo==0:
        messagebox.showerror("Error","Debe seleccionar una casilla en tiempo")
        return
    elif totaltiempo>1:
        messagebox.showerror("Error","Debe seleccionar solo una casilla en tiempo")
        return
    
    if gtsi==1:
        tiempo=1
    if gtno==1:
        tiempo=2
        
    ghoras=0
    gminutos=0
    gsegundos=0
    
    if gttimer==1:
        tiempo=3
        ghoras=entradah.get()
        if ghoras=="":
            ghoras=0
        else:
            if ghoras.isnumeric()==False or (int(ghoras)<0 or int(ghoras)>2):
                messagebox.showerror("Error", "Las horas deben estar entre 0 y 2")
                return
            else:
                ghoras=int(ghoras)
        
        gminutos=entradam.get()
        if gminutos=="":
            gminutos=0
        else:
            if gminutos.isnumeric()==False or (int(gminutos)<0 or int(gminutos)>60):
                messagebox.showerror("Error", "Los minutos deben estar entre 0 y 60")
                return
            else:
                gminutos=int(gminutos)
        
        gsegundos=entradas.get()
        if gsegundos=="":
            gsegundos=0
        else:
            if gsegundos.isnumeric()==False or (int(gsegundos)<0 or int(gsegundos)>60):
                messagebox.showerror("Error", "Los segundos deben estar entre 0 y 60")
                return
            else:
                gsegundos=int(gsegundos)
                
        if (ghoras+gminutos+gsegundos)==0:
            messagebox.showerror("Error", "Debe digitar al menos un valor en el temporizador")
            return
        
    gderecha=checkderecha.get()
    gizquierda=checkizquierda.get()
    glados=gderecha+gizquierda
        
    if glados==0:
        messagebox.showerror("Error","Debe seleccionar una casilla en Posición del panel de dígitos")
        return
    elif glados>1:
        messagebox.showerror("Error","Debe seleccionar solo una casilla en Posición del panel de dígitos")
        return

    if gderecha==1:
        lado=1
    if gizquierda==1:
        lado=2

    listaconfig=[dificultad,tiempo,ghoras,gminutos,gsegundos,lado]

#gráficos

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
    botonmedio=tkinter.Checkbutton(config, text="Medio",variable=checkmedio, onvalue=1, offvalue=0)
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
    
configuracion()







