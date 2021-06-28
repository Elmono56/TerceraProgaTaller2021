



#gráficos menú de inicio
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
