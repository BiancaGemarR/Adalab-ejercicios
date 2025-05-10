class Empleado:

    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

empleado1 = Empleado('Marc', 29, 1542.8)
empleado2 = Empleado('German', 58, 1450.6)
empleado3 = Empleado('Paqui', 58, 2145.5)
empleado4 = Empleado('Melania', 35, 5478.5)
empleado5 = Empleado('Ricard', 42, 4511.5)
empleado6 = Empleado('Mercedes', 61, 2145.5)
empleado7 = Empleado('Bianca', 31, 3500.5)

empleados = (empleado1, empleado2, empleado3, empleado4, empleado5, empleado6, empleado7)
sueldos_altos = [(e.name, e.salary) for e in empleados if e.salary > 2500]
print(sueldos_altos)

