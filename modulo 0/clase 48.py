#sumar vectores
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2 
#sobrecarga 
print(v3)

#comparación, igual
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad
    
p1 = Persona("Ana", 30)
p2 = Persona("Ana", 30)

print(p1==p2)

#comparación, menor que
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad
p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)
print(p1>p2)
print(p1<p2)

#sobrecarga de operador con fracciones

from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    def __add__(self, otra_fraccion):
        nuevo_num = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_den = self.denominador * otra_fraccion.denominador
        comun_divisor = gcd(nuevo_num, nuevo_den)
        return Fraccion(nuevo_num // comun_divisor, nuevo_den // comun_divisor)
    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"
    
f1 = Fraccion(1, 4)
f2 = Fraccion(1, 2)

f3 = f1 + f2  
print(f3) 
        
        

