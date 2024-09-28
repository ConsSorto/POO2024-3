"""
numero1 = int(input('Ingrese numero 1 : '))
numero2 = int(input('Ingrese numero 2 : '))

numero3 = 0
while (numero3 < numero1):
    numero3 = numero3 + 1
    producto = numero3 * numero2
    print(str(numero3) + " X " + str(numero2) + " = " + str(producto))

"""

arreglo = ['Cons', 'Mauricio', 'Lisis', 'Diana', 'Jose', 'Carlos']
for persona in arreglo:
    print("Bienvenido : " + persona)

print("-----------------------------------------------------------")

tamanoArreglo = len(arreglo)
i = 0
while i < tamanoArreglo:
    print("Bienvenido : " + arreglo[i])
    i+=1
