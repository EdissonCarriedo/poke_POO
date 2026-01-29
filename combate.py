class Combate:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def iniciar(self):
        print("¡Comienza el combate de Pokemones!\n")

        # Determinar quién inicia
        if self.p1.velocidad > self.p2.velocidad:
            atacante, defensor = self.p1, self.p2
        else:
            atacante, defensor = self.p2, self.p1

        turno = 1

        while self.p1.esta_vivo() and self.p2.esta_vivo():
            print(f"--- Turno {turno} ---")

            movimiento = atacante.elegir_movimiento()
            atacante.atacar(defensor, movimiento)

            atacante, defensor = defensor, atacante
            turno += 1

        self.mostrar_resultado()

    def mostrar_resultado(self):
        if self.p1.esta_vivo():
            print(f"{self.p1.nombre} gana el combate")
        else:
            print(f"{self.p2.nombre} gana el combate")
