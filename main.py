from pokemon import Pokemon
from movimiento import Movimiento
from combate import Combate

# Movimientos
impactrueno = Movimiento("Impactrueno", 1.0)
placaje = Movimiento("Placaje", 0.9)
aranazo = Movimiento("Arañazo", 0.8)
lanzallamas = Movimiento("Lanzallamas", 1.2)

# Pokemons con LISTA de movimientos
p1 = Pokemon(
    nombre="Pikachu",
    vida=135,
    ataque=15,
    defensa=5,
    velocidad=20,
    movimientos=[impactrueno, placaje]
)

p2 = Pokemon(
    nombre="Charmander",
    vida=140,
    ataque=18,
    defensa=6,
    velocidad=15,
    movimientos=[aranazo, lanzallamas]
)

combate = Combate(p1, p2)
combate.iniciar()
