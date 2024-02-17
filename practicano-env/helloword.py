from datetime import datetime
import os
import serial 

try:
    arduino = serial.Serial('/dev/cu.usbserial-140', 9600)
    print('Conectado a Arduino por las nalgas')
    fechahora = datetime.now()
    opcion = '0'
    estado_motor = 'detenido'
    while opcion != 'x':
        os.system('clear')
        print('DESARROLLADO POR TU PAPI CHULO')
        print("La fecha de hoy es ", fechahora.strftime("%A %d %B %Y %H:%M:%S"))
        print('El motor  se encuentra' , estado_motor)
        print('Selecciona una opción:')
        if opcion !='d' and opcion !='i' and opcion !='s' and opcion !='0':
            print('Opción no válida. \n El motor mantiene el estado anterior:' , estado_motor)
        opcion = input("\nEscribe\n 'd' para girar a la derecha\n'i' para girar a la izquierda\n's' para detener el motor\n'x' para salir: ")
        if opcion == 'd':
            estado_motor = 'girando a la derecha'
            arduino.write(b's')
            arduino.write(b'd')
        elif opcion == 'i':
            estado_motor = 'girando a la izquierda'
            arduino.write(b's')
            arduino.write(b'i')
        elif opcion == 's':
            estado_motor = 'detenido'
            arduino.write(b's')
        elif opcion == 'x':
            print('Saliendo del programa.')
    print('Motor apagado broh')
    arduino.close()
except:
    print('No se pudo conectar a Arduino', arduino.exception())