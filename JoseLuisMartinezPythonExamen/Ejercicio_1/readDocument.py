
class ReadDocument():
    def __init__(self):
        pass

    def leerFichero(self, num1, num2):
        filename = "tabla-%s.txt" %num1

        try:
            with open(filename) as f_obj:
                lines = f_obj.readlines()
                print(lines[num2 - 1])
                if not lines:
                    print("La tabla no se encuentra")
        except FileNotFoundError:
            print("El fichero no se encuentra, intenta nuevamente")

    def ingresaValores(self):
        numero1 = int(input("Ingresa el numero de la tabla que deseas abrir: "))
        numero2 = int(input("Ingresa el numero a multiplicar: "))
        self.leerFichero(numero1, numero2)

leyendoDocumento = ReadDocument().ingresaValores()