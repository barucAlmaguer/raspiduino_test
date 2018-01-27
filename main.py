import serial
import serial.tools.list_ports as lp

def portnames():
    lista = lp.comports()
    names = []
    for port in lista:
        names.append(port[0])
    return names

print("hola mundo")