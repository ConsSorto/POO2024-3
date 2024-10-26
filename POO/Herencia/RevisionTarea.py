class Persona:

    def __init__(self, nombre, apellido, id, direccion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion


class Visitante(Persona):
    def __init__(self, nombre, apellido, id, direccion, razon, edificio):
        super().__init__(nombre, apellido, id, direccion)
        self.razon = razon
        self.edificio = edificio

    def datos(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "direccion": self.direccion,
            "DNI": self.id,
            "razon": self.razon,
            "edificio": self.edificio
        }


class Alumno(Persona):
    def __init__(self, nombre, apellido, id, direccion, carrera, horario, cuenta):
        super().__init__(nombre, apellido, id, direccion)
        self.carrera = carrera
        self.horario = horario
        self.cuenta = cuenta

    def datos(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "direccion": self.direccion,
            "DNI": self.id,
            "carrera": self.carrera,
            "horario": self.horario,
            "cuenta": self.cuenta}


class Maestro(Persona):
    def __init__(self, nombre, apellido, id, direccion, facultad, especializacion, n_empleado):
        Persona.__init__(self, nombre, apellido, id, direccion)
        self.facultad = facultad
        self.especializacion = especializacion
        self.n_empleado = n_empleado

    def datos(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "direccion": self.direccion,
            "DNI": self.id,
            "facultad": self.facultad,
            "especializacion": self.especializacion,
            "num_empleado": self.n_empleado}


class Empleado(Persona):
    def __init__(self, nombre, apellido, id, direccion, num, area, trabajacf):
        Persona.__init__(self, nombre, apellido, id, direccion)
        self.num = num
        self.area = area
        self.trabajacf = trabajacf

    def datos(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "direccion": self.direccion,
            "DNI": self.id,
            "numero empleado": self.num,
            "area": self.area,
            "Trabajo": self.trabajacf}


class JefeCoordinador(Maestro, Empleado):
    def __init__(self, nombre, apellido, id, direccion, facultad, especializacion, n_empleado, num, area, trabajacf,
                 inicio, fin, cargo):
        Maestro.__init__(self, nombre, apellido, id, direccion, facultad, especializacion, n_empleado)
        Empleado.__init__(self, nombre, apellido, id, direccion, num, area, trabajacf)
        self.inicio = inicio
        self.fin = fin
        self.cargo = cargo

    def datos(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "direccion": self.direccion,
            "DNI": self.id,
            "facultad": self.facultad,
            "especializacion": self.especializacion,
            "num_empleado": self.n_empleado,
            "area": self.area,
            "Trabajo": self.trabajacf,
            "Inicio": self.inicio,
            "Fin": self.fin,
            "cargo": self.cargo
        }


class metodos:
    @staticmethod
    def pedir_nombre():
        dato = input("ingrese su nombre:")
        return dato

    @staticmethod
    def pedir_apellido():
        dato = input("ingrese su apellido:")
        return dato

    @staticmethod
    def pedir_id():
        dato = input("ingrese su identidad:")
        return dato

    @staticmethod
    def pedir_direccion():
        dato = input("ingrese su direcccion:")
        return dato

    # metodos para la clase visitante
    @staticmethod
    def pedir_razon():
        dato = input("ingrese cual es la razon de su visita:")
        return dato

    @staticmethod
    def pedir_edificio():
        dato = input("ingrese el edificio al cual se dirije:")
        return dato

    # metodos de la clase Alumno

    @staticmethod
    def pedir_carrera():
        dato = input("ingrese la carrera a la que pertenece:")
        return dato

    @staticmethod
    def pedir_horario():
        dato = input("ingrese su horario:")
        return dato

    @staticmethod
    def pedir_cuenta():
        dato = input("ingrese su numero de cuanta:")
        return dato

    # metodos de la clase maestro
    @staticmethod
    def pedir_faultad():
        dato = input("ingrese la faculta a la que pertenece:")
        return dato

    @staticmethod
    def pedir_especializacion():
        dato = input("ingrese su especializacion:")
        return dato

    @staticmethod
    def pedir_nempleado():
        dato = input("ingrese su numero de empleado:")
        return dato

    # metodos de la clase empleado
    @staticmethod
    def pedir_area():
        dato = input("ingrese el area en la que labora:")
        return dato

    @staticmethod
    def pedir_lugar():
        dato = input("ingrese donde labora campo o oficina:")
        return dato

    # clase jefe o corrdinador
    @staticmethod
    def pedir_inicio():
        dato = input("ingrese cuando inicio su cargo:")
        return dato

    @staticmethod
    def pedir_fin():
        dato = input("ingrese cuando finaliza su cargo:")
        return dato

    @staticmethod
    def pedir_cargo():
        dato = input("ingrese el cargo que ejecuta:")
        return dato

    @staticmethod
    def menu():
        menu_data = ["1.Registrar visita", "2.ver historial de visitas", "3.salir"]
        for i in menu_data:
            print(i)
        print()
        dato = int(input("ingrese la opcion que necesita:"))
        return dato

    @staticmethod
    def seleccion():
        selec = ["1.Visitante", "2.Alumno", "3.Maestro", "4.Empleado", "5.Jefe o coordinador"]
        for a in selec:
            print(a)
        print()
        dato = int(input("ingrese que tipo de visitante es:"))
        return dato


print("\tUniversidad Nacional Autonoma de Honduras")
registro = []
while True:
    match metodos.menu():
        case 1:
            match metodos.seleccion():
                case 1:
                    particular = Visitante(metodos.pedir_nombre(), metodos.pedir_apellido(), metodos.pedir_id(),
                                           metodos.pedir_direccion(), metodos.pedir_razon(), metodos.pedir_edificio())

                    registro.append(particular.datos())
                case 2:
                    estudiante = Alumno(metodos.pedir_nombre(), metodos.pedir_apellido(), metodos.pedir_id(),
                                        metodos.pedir_direccion()
                                        , metodos.pedir_carrera(), metodos.pedir_horario(), metodos.pedir_cuenta())
                    registro.append(estudiante.datos())
                case 3:
                    docente = Maestro(metodos.pedir_nombre(), metodos.pedir_apellido(), metodos.pedir_id(),
                                      metodos.pedir_direccion(),
                                      metodos.pedir_faultad(), metodos.pedir_especializacion(),
                                      metodos.pedir_nempleado())
                    registro.append(docente.datos())
                case 4:
                    colab = Empleado(metodos.pedir_nombre(), metodos.pedir_apellido(), metodos.pedir_id(),
                                     metodos.pedir_direccion(),
                                     metodos.pedir_nempleado(), metodos.pedir_area(), metodos.pedir_lugar())
                    registro.append(colab.datos())
                case 5:
                    boss = JefeCoordinador(metodos.pedir_nombre(), metodos.pedir_apellido(), metodos.pedir_id(),
                                           metodos.pedir_direccion(), metodos.pedir_faultad(),
                                           metodos.pedir_especializacion(), metodos.pedir_nempleado(),
                                           metodos.pedir_nempleado(), metodos.pedir_area(), metodos.pedir_lugar(),
                                           metodos.pedir_inicio(), metodos.pedir_fin(), metodos.pedir_cargo())

                    registro.append(boss.datos())

        case 2:
            print(registro)
        case 3:
            break
