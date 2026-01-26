# poke_POO
# CLASE POKEMON
# OBJETO --> NOMBRE DEL POKEMON
# ATRIBUTOS --> NOMBRE, TIPO, VIDA
# METODOS ---> ACCIONES QUE PUEDE HACER EL OBJETO CREADO COMO:
- ATACAR
- MOSTRAR VIDA

  # EN PYTHON:
  # 1. CREAR LA CLASE POKEMON

      class Pokemon:
        def __init__(self, nombre, vida):
           self.nombre = nombre
           self.vida = vida

        def atacar(self, otro):
          print(f"{self.nombre} ataca a {otro.nombre}!")
          otro.vida -= 10  # siempre quita 10 de vida
          if otro.vida < 0:
            otro.vida = 0

        def mostrar_vida(self):
          print(f"{self.nombre} tiene {self.vida} de vida")

  # 2. CREAR LOS POKEMON

      pikachu = Pokemon("Pikachu", 50)
      bulbasaur = Pokemon("Bulbasaur", 50)

  # 3. BATALLA SIMPLE

      pikachu.mostrar_vida()
      bulbasaur.mostrar_vida()

      pikachu.atacar(bulbasaur)
      bulbasaur.atacar(pikachu)

      pikachu.mostrar_vida()
      bulbasaur.mostrar_vida()

# SALIDA ESPERADA

  Pikachu tiene 50 de vida
  
  Bulbasaur tiene 50 de vida
  
  Pikachu ataca a Bulbasaur!
  
  Bulbasaur ataca a Pikachu!
  
  Pikachu tiene 40 de vida
  
  Bulbasaur tiene 40 de vida

  # RESUMEN Esto es POO de manera sencilla:

  Clase: Pokemon → el molde

  Objeto: pikachu, bulbasaur → los Pokémon concretos

  Atributos: nombre, vida

  Métodos: atacar(), mostrar_vida()


