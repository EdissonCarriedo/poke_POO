class Movimiento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.__movimientos = []  # encapsulación (atributo privado)

    def agregar_movimiento(self, movimiento):
        if movimiento.tipo != self.tipo:
            print(f"El movimiento {movimiento.nombre} no es del mismo tipo que el Pokémon.")
            return

        if len(self.__movimientos) >= 4:
            print(f"El Pokémon {self.nombre}  ya tiene 4 movimientos.")
            return

        self.__movimientos.append(movimiento)
        print(f"Movimiento {movimiento.nombre} agregado a {self.nombre}")

    def sustituir_movimiento(self, indice, nuevo_movimiento):
        if nuevo_movimiento.tipo != self.tipo:
            print(f"El nuevo movimiento no es del mismo tipo {self.tipo}")
            return

        if indice < 0 or indice >= len(self.__movimientos):
            print("Índice de movimiento inválido.")
            return

        eliminado = self.__movimientos[indice]
        self.__movimientos[indice] = nuevo_movimiento
        print(f"Movimiento {eliminado.nombre} fue reemplazado por {nuevo_movimiento.nombre}.")

    def mostrar_movimientos(self):
        print(f"\n Movimientos de {self.nombre}:")
        
        for i, mov in enumerate(self.__movimientos, start= 1):
            print(f"{i}. {mov}")

# Crear Pokémon
pikachu = Pokemon("Pikachu", "Eléctrico")

# Crear movimientos
impactrueno = Movimiento("Impactrueno", "Eléctrico")
rayo = Movimiento("Rayo", "Eléctrico")
trueno = Movimiento("Trueno", "Eléctrico")
placaje = Movimiento("Placaje", "Normal")  # tipo incorrecto
voltio = Movimiento("Voltio Cruel", "Eléctrico")

# Agregar movimientos
pikachu.agregar_movimiento(impactrueno)
pikachu.agregar_movimiento(rayo)
pikachu.agregar_movimiento(trueno)
pikachu.agregar_movimiento(voltio)
pikachu.agregar_movimiento(placaje)  # no se permite

pikachu.mostrar_movimientos()

# Sustituir un movimiento
nuevo = Movimiento("Electrocañón", "Eléctrico")
pikachu.sustituir_movimiento(3, nuevo)

pikachu.mostrar_movimientos()

