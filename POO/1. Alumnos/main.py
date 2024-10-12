from Alumno import Alumno

alumno = input("Ingrese su alumno: ")
nota1 = int(input("Ingrese Nota 1 :"))
nota2 = int(input("Ingrese Nota 2 :"))
nota3 = int(input("Ingrese Nota 3 :"))
nota4 = int(input("Ingrese Nota 4 :"))

alumno = Alumno(alumno, nota1, nota2, nota3, nota4)
alumno.calcularPromedio()
print(alumno.DatosAlumno())