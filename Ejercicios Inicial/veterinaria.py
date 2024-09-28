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
    print(citasDelDia)

    menu = ["1. Agregar", "2. Modificar", "3. Eliminar", "4. Buscar por nombre", "5. Llamar proximo", "6. Salir"]

    for item in menu:
        print(item)

    item = int(input("Ingrese opcion :"))

    if item == 1:
        #cita = { 'estado' : 'esperando', 'nombre' : '', 'peso':0,'dueno':''}
        cita = {'estado': 'esperando'}
        cita['nombre'] = input("Ingrese nombre animal :")
        cita['peso'] = input("Ingrese peso del animal :")
        cita['dueno'] = input("Ingrese dueño del animal :")
        citasDelDia.append(cita)

    elif item == 2:
        numeroCita = int(input("Ingrese Numero de Cita a Modificar : "))
        citaModificar = citasDelDia[numeroCita-1]
        citaModificar['nombre'] = input("Ingrese nombre animal :")
        citaModificar['peso'] = input("Ingrese peso del animal :")
        citaModificar['dueno'] = input("Ingrese dueño del animal :")
        citasDelDia[numeroCita-1] = citaModificar

    elif item == 3:
        numeroCita = int(input("Ingrese Numero de Cita a Eliminar : "))
        citasDelDia.pop(numeroCita-1)

    elif item == 4:
        dueno = input("Ingrese Dueño : ")
        encontrado = False
        for cita in citasDelDia:
            if cita['dueno'].upper() == dueno.upper():
                print(cita)
                encontrado = True
        if not encontrado:
            print("No encontrado")

    elif item == 5:
        for cita in citasDelDia:
            if cita['estado'] == "en proceso":
                cita['estado'] = "finalizada"
            if cita['estado'] == "esperando":
                print("Se requiere al animal : " + cita['nombre'])
                cita['estado'] = "en proceso"
                break
    elif item == 6:
        print("Gracias")
        salir = True



