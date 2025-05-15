class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Devuelve una representación amigable para el usuario
    def __str__(self):
        return f'Persona: {self.nombre}, {self.edad} años'  
    
    # Devuelve una representación detallada del objeto para depuración
    def __repr__(self):
        return f'<Persona(nombre={self.nombre}, edad={self.edad})>'
    
     # Compara si dos personas son iguales en función del nombre y la edad
    def __eq__(self, other):
        return self.nombre == other.nombre and self.edad == other.edad
    
    # Compara si una persona es "menor" que otra en función de la edad
    def __lt__(self, other):
        return self.edad < other.edad

     # 
    def __le__(self, other):
        return self.edad <= other.edad
     # Sobrecarga el operador + para sumar las edades de dos personas
    def __add__(self, other):
        return self.edad + other.edad
p1 = Persona('Ana', 28)
p3 = Persona('Juan', 35)
resultado = p1 + p3  
# Esto devuelve 63
print(p1)
print(p3)
print(resultado)