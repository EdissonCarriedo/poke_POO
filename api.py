from fastapi import FastAPI
from pokemon import Pokemon
from movimiento import Movimiento
from combate import Combate

app = FastAPI()

# Crear movimientos
impactrueno = Movimiento("Impactrueno", 1.0)
placaje = Movimiento("Placaje", 0.9)
aranazo = Movimiento("Arañazo", 0.8)
lanzallamas = Movimiento("Lanzallamas", 1.2)

# Crear pokemons
p1 = Pokemon(
    nombre="Pikachu",
    tipo="Eléctrico",
    vida=135,
    ataque=15,
    defensa=5,
    velocidad=20,
    movimientos=[impactrueno, placaje]
)

p2 = Pokemon(
    nombre="Charmander",
    tipo="Fuego",
    vida=140,
    ataque=18,
    defensa=6,
    velocidad=15,
    movimientos=[aranazo, lanzallamas]
)

# Endpoint para ver pokemons
@app.get("/pokemons")
def obtener_pokemons():
    return {
        "Pikachu": [m.nombre for m in p1.movimientos],
        "Charmander": [m.nombre for m in p2.movimientos]
    }

# Endpoint para iniciar combate
@app.get("/combate")
def iniciar_combate():
    combate = Combate(p1, p2)
    resultado = combate.iniciar()
    return {"resultado": resultado}
