class Vehiculo():
    def __init__(self, marca, modelo, año):
        # Encapsulamiento: Los atributos están encapsulados con doble guion bajo (__).
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    # Encapsulamiento: Métodos getter y setter.
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año

    # Polimorfismo: Este método será sobreescrito en las clases derivadas.
    def detener(self):
        print(f"El vehículo {self.get_marca()} {self.get_modelo()} se ha detenido.")


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        # Herencia: Llamada al constructor de la clase base.
        super().__init__(marca, modelo, año)
        self.__puertas = puertas

    # Polimorfismo: Sobrescritura del método acelerar.
    def acelerar(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} está acelerando.")

    # Polimorfismo: Sobrescritura del método detener.
    def detener(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} se ha detenido.")


# Abstracción: Las clases derivadas implementan detalles específicos.
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    def acelerar(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} con cilindrada de {self.get_cilindrada()}cc está acelerando.")

    def detener(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} se ha detenido.")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.__capacidad_carga = capacidad_carga

    def acelerar(self):
        print(f"El camión {self.get_marca()} {self.get_modelo()} con capacidad de {self.get_capacidad_carga()} toneladas está acelerando.")

    def detener(self):
        print(f"El camión {self.get_marca()} {self.get_modelo()} se ha detenido.")
