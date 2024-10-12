from Cita import Cita
from utils import Utils
"""
Veterinaria

Es encargarse de guardar los datos de las citas
estado: esperando, en proceso, finalizada
animal : nombre, peso, dueno

agregar, modificar, eliminar y buscar
funcion de agragar llamado.
"""
citasDelDia = []
salir = False
while(not salir):

    for arrraycita in citasDelDia:
        print(arrraycita)

    Utils.crearMenu()

    item = int(input("Ingrese opcion :"))

    if item == 1:
        nombre, peso, dueno = Utils.obtenerDatos()
        cita = Cita(nombre, peso, dueno)
        citasDelDia.append(cita)
    elif item == 2:
        numeroCita = int(input("Ingrese Numero de Cita a Modificar : "))
        citaModificar = citasDelDia[numeroCita-1]
        nombre, peso, dueno = Utils.obtenerDatos()
        citaModificar.nombre = nombre
        citaModificar.peso = peso
        citaModificar.dueno = dueno
        citasDelDia[numeroCita-1] = citaModificar
    elif item == 3:
        numeroCita = int(input("Ingrese Numero de Cita a Eliminar : "))
        citasDelDia.pop(numeroCita-1)
    elif item == 4:
        dueno = input("Ingrese Dueño : ")
        encontrado = False
        for cita in citasDelDia:
            if cita.dueno.upper() == dueno.upper():
                print(cita)
                encontrado = True
        if not encontrado:
            print("No encontrado")
    elif item == 5:
        Utils.llamarProximo(citasDelDia)
    elif item == 6:
        print("Gracias")
        salir = True



