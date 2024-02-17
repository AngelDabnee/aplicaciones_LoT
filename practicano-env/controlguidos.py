from tkinter import Tk, Label, Button, PhotoImage
import serial
import time
from PIL import Image, ImageTk  


#funciones de la aplicación
def actualizar_fecha():
    # Actualizar la fecha y hora actuales en el label
    fecha_actual = time.strftime("%A %d %B %Y %H:%M:%S")
    label_fecha.config(text=fecha_actual)
    # Programar la próxima actualización para dentro de 1000ms (1 segundo)
    ventana.after(1000, actualizar_fecha)

def mover_derecha():
    estado_motor.config(text="El motor se encuentra: moviendo a la derecha")
    botton_derecha.config(state="disabled")
    botton_izquierda.config(state="normal")
    botton_paro.config(state="normal")
    try:
        arduino.write(b's')
        arduino.write(b'd')
    except:
        print('No se pudo conectar a Arduino')
    
    

def mover_izquierda():
    estado_motor.config(text="El motor se encuentra: moviendo a la izquierda")
    botton_derecha.config(state="normal")
    botton_izquierda.config(state="disabled")
    botton_paro.config(state="normal")
    try:
        arduino.write(b's')
        arduino.write(b'i')
    except:
        print('No se pudo conectar a Arduino')


def detener_motor():
    estado_motor.config(text="El motor se encuentra: detenido")
    botton_derecha.config(state="normal")
    botton_izquierda.config(state="normal")
    botton_paro.config(state="disabled")
    try:
        arduino.write(b's')
    except:
        print('No se pudo conectar a Arduino')

def redimensionar_imagen(ruta_imagen, nuevo_ancho, nuevo_alto):
    imagen = Image.open(ruta_imagen)
    imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))
    return ImageTk.PhotoImage(imagen_redimensionada)
    
def establecer_fondo(ventana, ruta_imagen):
    # Cargar la imagen usando PIL
    imagen = Image.open(ruta_imagen)
    # Redimensionar la imagen al tamaño de la ventana
    imagen = imagen.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
    # Convertir la imagen de PIL a PhotoImage de Tkinter
    foto = ImageTk.PhotoImage(imagen)
    # Crear un Label para mostrar la imagen y expandirlo para llenar la ventana
    label_fondo = Label(ventana, image=foto)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    # Mantener una referencia de la imagen para evitar que sea eliminada por el recolector de basura
    label_fondo.image = foto
    

    

try:
    arduino = serial.Serial('/dev/cu.usbserial-11320', 9600)
except:
    print('No se pudo conectar a Arduino')


ventana = Tk()
ventana.title('Sistema de control de motor de corriente directa')
establecer_fondo(ventana, './img/waifus.png')
ventana.state("zoomed")

etiqueta = Label(ventana, text="DESARROLLADO POR: TU PAPI CHULO", bg="#58d1c5", font=("Arial Bold", 20))
nombre_proyecto = Label(ventana, text="Sistema de control de motor de corriente directa", bg="#58d1c5", font=("Arial Bold", 20))

label_fecha = Label(ventana, bg="#58d1c5", font=("Arial Bold", 20))

ventana.update_idletasks()  
ancho_ventana = ventana.winfo_width()
ancho_etiqueta = etiqueta.winfo_reqwidth()

x_pos = (ancho_ventana - ancho_etiqueta) / 2
etiqueta.place(x=x_pos, y=50)
nombre_proyecto.place(x=x_pos-30, y=100 + 50)  # Ajustado para que esté debajo de etiqueta
label_fecha.place(x=x_pos-30, y=150 + 100) 



# Colocar label_fecha debajo de nombre_proyecto con un pequeño margen adicional
label_fecha.place(x=x_pos-30, y=150 + 50)  # Ajusta el valor de y según sea necesario

estado_motor = Label(ventana, text="El motor se encuentra: detenido", bg="#58d1c5", font=("Arial Bold", 20))
estado_motor.place(x=x_pos, y=700)

ancho_imagen =300
alto_imagen = 300   

img_derecha = redimensionar_imagen("./img/imagenDerechaSinFondo.png",ancho_imagen,alto_imagen)
botton_derecha = Button(ventana, image=img_derecha, command=mover_derecha)
botton_derecha.place(x=1000, y=300)

img_izq = redimensionar_imagen("./img/izquierda.png",ancho_imagen,alto_imagen)
botton_izquierda = Button(ventana, image=img_izq, command=mover_izquierda)
botton_izquierda.place(x=200, y=300)

img_paro = redimensionar_imagen("./img/paro-removebg-preview.png",ancho_imagen,alto_imagen)  
botton_paro = Button(ventana, image=img_paro, command=detener_motor,state="disabled")
botton_paro.place(x=600, y=300)

actualizar_fecha()  # Iniciar el proceso de actualización de la fecha y hora


ventana.mainloop()
try:
    arduino.close()
except:
    print('No se pudo conectar a Arduino')
