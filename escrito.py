


#import time

#while True:

    #print("cada segundo")

    #time.sleep(1)







#from tkinter import messagebox

#siono=messagebox.askyesno("","Decidir entre sí o no")

#if siono==True:
    #messagebox.showinfo("","Se decidió sí")
#else:
    #messagebox.showinfo("","Se decidió no")

def bloquear(entrada):

    entrada.config(state="disable")

import tkinter

ventana=tkinter.Tk()
ventana.geometry("200x100")

lcorreo=tkinter.Label(ventana,text="Digite su correo")
lcorreo.pack()

entrada=tkinter.Entry(ventana)
entrada.pack()

boton=tkinter.Button(ventana,text="Aceptar",command=lambda:[bloquear(entrada)])
boton.pack()

ventana.mainloop()



