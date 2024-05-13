class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.__nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def toString(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.edad}, Ciudad {self.ciudad}")

    def getNombre(self):
        return self.__nombre