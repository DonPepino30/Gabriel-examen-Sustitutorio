import random
from datetime import datetime

def numeroAleatorio():
    return random.randint(1, 50)

def ingresarNumero():
    while True:
        try:
            while True:
                numero = int(input("Ingrese un numero entre 1 y 100: "))
                if numero > 1 and numero < 100:
                    return numero
                else:
                    print("ERROR! El numero debe estar entre 1 y 100")
        except ValueError as e:
            print(e)

def Adivinar():
    numeroRandom = numeroAleatorio()
    numeroIngresado = ingresarNumero()

    while numeroIngresado != numeroRandom:
        if numeroIngresado > numeroRandom:
            print("El numero ingresado es mayor!")
        else:
            print("El numero ingresado es menor!")
        numeroIngresado = ingresarNumero()

    print(f"Has ganado! El numero fue {numeroRandom}")
    print(f"La fecha actual es {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def decorador(func):
    def funcA(*args, **kwargs):
        print("Antes de adivinar:")
        resultado = func(*args, **kwargs)
        print("Luego de adivinar:")
        return resultado
    return funcA

@decorador
def main():
    Adivinar()

if __name__ == "__main__":
    main()