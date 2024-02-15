class Vehicle:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}")


class Carro(Vehicle):
    def __init__(self, marca, modelo, color, tipo_carroceria):
        super().__init__(marca, modelo, color)
        self.tipo_carroceria = tipo_carroceria

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de carrocería: {self.tipo_carroceria}")


class Barco(Vehicle):
    def __init__(self, marca, modelo, color, eslora):
        super().__init__(marca, modelo, color)
        self.eslora = eslora

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Eslora: {self.eslora} metros")


class Avion(Vehicle):
    def __init__(self, marca, modelo, color, envergadura):
        super().__init__(marca, modelo, color)
        self.envergadura = envergadura

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Envergadura: {self.envergadura} metros")


def registrar_vehiculo(tipo):
    marca = input(f"Ingrese la marca del {tipo}: ")
    modelo = input(f"Ingrese el modelo del {tipo}: ")
    color = input(f"Ingrese el color del {tipo}: ")

    if tipo == "carro":
        tipo_carroceria = input("Ingrese el tipo de carrocería del carro: ")
        return Carro(marca, modelo, color, tipo_carroceria)
    elif tipo == "barco":
        eslora = float(input("Ingrese la eslora del barco en metros: "))
        return Barco(marca, modelo, color, eslora)
    elif tipo == "avion":
        envergadura = float(input("Ingrese la envergadura del avión en metros: "))
        return Avion(marca, modelo, color, envergadura)
    else:
        raise ValueError("Tipo de vehículo no válido")


def main():
    vehiculos = []

    while True:
        print("\n¿Qué tipo de vehículo desea registrar?")
        print("1. Carro")
        print("2. Barco")
        print("3. Avión")
        print("4. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            vehiculo = registrar_vehiculo("carro")
            vehiculos.append(vehiculo)
        elif opcion == "2":
            vehiculo = registrar_vehiculo("barco")
            vehiculos.append(vehiculo)
        elif opcion == "3":
            vehiculo = registrar_vehiculo("avion")
            vehiculos.append(vehiculo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    print("\nInformación de los vehículos registrados:")
    for vehiculo in vehiculos:
        vehiculo.mostrar_informacion()


if __name__ == "__main__":
    main()
