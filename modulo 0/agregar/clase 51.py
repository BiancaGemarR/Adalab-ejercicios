class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs
    def show_employee(self):
        print (f'Employee: {self.name}')
        print (f'Employee: {self.skills}')
        print (f'EMployee: {self.details}')

employee1 = Employee('Carlos', 'python', 'java', 'c++', age= 30, city = 'bogota')
employee1.show_employee()

        