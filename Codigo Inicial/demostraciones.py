"""
miVariable = "Esto es un string"
miVariable2 = " de la clase POO"
mivariable3 = miVariable + miVariable2
print(mivariable3)

print(mivariable3 * 4)
"""

integer = 1
floatante = 1.1
string = "Esto es un string"
boleano = True
diccionatio  = {'clave' : "valor", "nombre" : "Constantino Sorto"}
lista = [1,2,3]
tupla = (1,2,3)

if integer > 2:
    print("entro al if")
    print("nueva linea")
elif floatante > 1:
    print("entro al elif")
else:
    print("entro al else")
    print("nueva linea")

print("esto no esta en el if")

"""
lecturaConsulta = input("Ingrese un valor")

if lecturaConsulta == "ClasePoo":
    print("Muy Bien")
else:
    print("Muy Mal")
"""


lecturaInteger = input("Ingrese un Entero :")
print(type(lecturaInteger))

try:
    #Posiblemente me de error
    miEntero = int(lecturaInteger)
    print("El numero es " + str(miEntero))
except:
    #Codigo por si da error
    print("El valor no se puede convertir a entero")
else:
    # Codigo que se va ejecutar si no da error
    print("codigo general siempre que no de error")


# Lisis solicito codigo para pedir de nuevo entero si da error

ejecutarse = True

while(ejecutarse):
    lecturaInteger = input("Ingrese un Entero :")
    try:
        # Posiblemente me de error
        miEntero = int(lecturaInteger)
        print("El numero es " + str(miEntero))
        ejecutarse = False
    except:
        #Codigo por si da error
        print("El valor no se puede convertir a entero")
    else:
        # Codigo que se va ejecutar si no da error
        print("codigo general siempre que no de error")

while(ejecutarse):
    try:
        miEntero = int(input("Ingrese un Entero :"))
        print("El numero es " + str(miEntero))
        ejecutarse = False
    except:
        #Codigo por si da error
        print("El valor no se puede convertir a entero")
    else:
        # Codigo que se va ejecutar si no da error
        print("codigo general siempre que no de error")