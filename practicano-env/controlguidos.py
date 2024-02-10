from tkinter import Tk, Label, Button, PhotoImage
import serial

def mover_derecha():
    estado_motor.config(text="El motor se encuentra: moviendo a la derecha")

def mover_izquierda():
    estado_motor.config(text="El motor se encuentra: moviendo a la izquierda")

def detener_motor():
    estado_motor.config(text="El motor se encuentra: detenido")

ventana = Tk()
ventana.title('Sistema de control de motor de corriente directa')
ventana['bg'] = '#58d1c5'
ventana.state("zoomed")

etiqueta = Label(ventana, text="DESARROLLADO POR: TU PAPI CHULO", bg="#58d1c5", font=("Arial Bold", 20))
nombre_proyecto = Label(ventana, text="Sistema de control de motor de corriente directa", bg="#58d1c5", font=("Arial Bold", 20))

ventana.update_idletasks()  
ancho_ventana = ventana.winfo_width()
ancho_etiqueta = etiqueta.winfo_reqwidth()

x_pos = (ancho_ventana - ancho_etiqueta) / 2
etiqueta.place(x=x_pos, y=50)
nombre_proyecto.place(x=x_pos-30, y=100)

estado_motor = Label(ventana, text="El motor se encuentra: detenido", bg="#58d1c5", font=("Arial Bold", 20))
estado_motor.place(x=x_pos, y=700)

img_derecha = PhotoImage(file = "./img/derecha.png")
botton_derecha = Button(ventana, image=img_derecha, command=mover_derecha)
botton_derecha.place(x=200, y=200)

img_izq = PhotoImage(file = "./img/izquierda.png")
botton_izquierda = Button(ventana, image=img_izq, command=mover_izquierda)
botton_izquierda.place(x=600, y=200)

img_paro = PhotoImage(file = "./img/paro.png")  
botton_paro = Button(ventana, image=img_paro, command=detener_motor)
botton_paro.place(x=1000, y=200)

ventana.mainloop()