# Definición de la clase Persona
class Persona:
    # Atributos de clase (no son necesarios en este caso,
    # porque luego se definen como atributos de instancia en __init__)
    nombre=""
    edad=20
    altura=0
    genero=""

    # Método constructor: se ejecuta automáticamente
    # cuando se crea un nuevo objeto de la clase Persona
    def __init__(self, nombre,edad,altura,genero):
        # Atributos de instancia (propios de cada objeto)
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        self.genero=genero

    # Método que devuelve un mensaje con los datos de la persona
    def caminar(self):
        return f"Hola soy {self.nombre} Estoy Caminado tengo mi edad {self.edad} mi altura es: {self.altura} y mi genero es: {self.genero}"

# Creación de un objeto (instancia) de la clase Persona
persona1= Persona("Danilo",40,1.79,"Masculino")


# Imprime los atributos del objeto persona1
print(persona1.nombre)
print(persona1.edad)
print(persona1.altura)
print(persona1.genero)


print(persona1.caminar())
