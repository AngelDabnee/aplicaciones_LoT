from datetime import datetime
import os




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
    elif opcion == 'i':
        estado_motor = 'girando a la izquierda'
    elif opcion == 's':
        estado_motor = 'detenido'
    elif opcion == 'x':
        print('Saliendo del programa.')
print('Motor apagado broh')
