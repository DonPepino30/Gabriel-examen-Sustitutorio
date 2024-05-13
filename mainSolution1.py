from Empleado import Empleado

def main():
    listaEmpleados = []
    while True:
        try:
            nombre = input("Ingrese su nombre: ")
            while True:
                edad = int(input("Ingrese su edad: "))
                if edad > 18 and edad < 80:
                    break
                else:
                    print("ERROR! La edad debe ser entre 18 y 80")
            ciudad = input("Ingrese su ciudad: ")
            salario = float(input("Ingrese su salario: "))
            empleado = Empleado(nombre, edad, ciudad, salario)
            listaEmpleados.append(empleado)
            print("Empleado agregado exitosamente!")
            opcion = input("Desea agregar otro empleado? (s/n): ")
            if opcion.lower() != "s":
                break
        except ValueError:
            print("Error!: Edad o salario deben ser números")
        except Exception as e:
            print(f"Error: {str(e)}")

    nombreArchivo = "empleados.txt"

    for empleado in listaEmpleados:
        empleado.generarArchivoEmpleado(nombreArchivo)
        print(empleado.manejoDiccionario())

    print("Empleados registrados:")
    listaEmpleados = Empleado.leerArchivoEmpleado(nombreArchivo)

    for empleado in listaEmpleados:
        print(f"Nombre: {empleado[0]}, Salario: {empleado[1]}, Impuesto: {empleado[2]}")

    nombre = input("Ingrese el nombre del empleado a buscar: ")
    Empleado.encontrarEmpleado(nombreArchivo, nombre)

if __name__ == "__main__":
    main()