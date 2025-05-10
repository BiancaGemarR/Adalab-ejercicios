class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
    def introduce(self) -> str:
        return f"hola me llamo {self.name} y tengo {self.age} años"
    
employee1 = Employee ('Carlos', 35, 1265.9)
print(employee1.introduce())

                     
    