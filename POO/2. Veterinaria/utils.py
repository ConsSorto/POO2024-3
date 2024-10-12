class Utils:
    @staticmethod
    def crearMenu():
        menu = ["1. Agregar", "2. Modificar", "3. Eliminar", "4. Buscar por nombre", "5. Llamar proximo", "6. Salir"]

        for item in menu:
            print(item)

    @staticmethod
    def obtenerDatos():
        nombre = input("Ingrese nombre animal :")
        peso = input("Ingrese peso del animal :")
        dueno = input("Ingrese dueño del animal :")

        return nombre, peso, dueno
    @staticmethod
    def llamarProximo(citasDelDia):
        for cita in citasDelDia:
            if cita.estado == "en proceso":
                cita.estado = "finalizada"
            if cita.estado == "esperando":
                print("Se requiere al animal : " + cita.nombre)
                cita.estado = "en proceso"
                break