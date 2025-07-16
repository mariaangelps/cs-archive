class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def imprimir(self):
        print('El nombre de la mascota es:', self.nombre)
        print('La edad de la mascota es:', self.edad)
        print('La raza de la mascota es:', self.raza)

def main():
    mascota = Mascota('Chloe', 3, 'Labrador')
    mascota.imprimir()

if __name__ == "__main__":
    main()
