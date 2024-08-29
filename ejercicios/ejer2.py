if __name__ == "__main__":
    vehiculos = {
        "Corolla": Auto("Toyota", "Corolla", 2020, 4),
        "MT-07": Motocicleta("Yamaha", "MT-07", 2019, 689),
        "Actros": Camion("Mercedes-Benz", "1620", 1980, 700)
    }


    for modelo, vehiculo in vehiculos.items():
        vehiculo.acelerar()
