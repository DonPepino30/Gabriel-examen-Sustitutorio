from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, ciudad, salario):
        super().__init__(nombre, edad, ciudad)
        self.salario = salario

    def impuesto(self):
        if self.salario > 5500:
            impuesto1 = self.salario * 0.09
            return impuesto1
        else:
            return 0

    def manejoDiccionario(self):
        return {
            "nombre": self.getNombre(),
            "edad": self.edad,
            "salario": self.salario,
            "impuesto": self.impuesto()
        }

    def generarArchivoEmpleado(self, nombreArchivo):
        with open(nombreArchivo, "a") as f:
            f.write(f"{self.getNombre()},{self.salario},{self.impuesto()}\n")

    @staticmethod
    def leerArchivoEmpleado(nombreArchivo):
        with open(nombreArchivo, "r") as f:
            empleados = [line.strip().split(",") for line in f.readlines()]
            return empleados

    @staticmethod
    def encontrarEmpleado(nombreArchivo, nombre):
        empleados = Empleado.leerArchivoEmpleado(nombreArchivo)
        for empleado in empleados:
            if empleado[0] == nombre:
                print(f"El empleado {nombre} tiene remuneración de {empleado[1]} y un impuesto de {empleado[2]}")
                return
        print(f"El empleado {nombre} no fue encontrado")
