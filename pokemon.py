import random

class Pokemon:
    def __init__(self, nombre, vida, ataque, defensa, velocidad, movimientos):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.movimientos = movimientos  # lista de Movimiento

    def esta_vivo(self):
        return self.vida > 0

    def elegir_movimiento(self):
        return random.choice(self.movimientos)

    def atacar(self, otro_pokemon, movimiento):
        dano_base = self.ataque - otro_pokemon.defensa
        if dano_base < 1:
            dano_base = 1

        dano_final = int(dano_base * movimiento.dano_porcentaje)
        otro_pokemon.vida -= dano_final

        print(f"{self.nombre} usa {movimiento.nombre}")
        print(f"{otro_pokemon.nombre} recibe {dano_final} de daño")
        print(f"Vida restante de {otro_pokemon.nombre}: {otro_pokemon.vida}\n")
