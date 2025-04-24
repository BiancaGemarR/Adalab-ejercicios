class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.available = True

    def buy(self):
        if self.available:
         self.available = False
         print(f"el coche {self.brand} está disponible")
        else:
         print(f"el coche {self.brand} no está disponible")

class user:
   def __init__(self, name, user_id):
      self.name = name
      self.user_id = user_id
      self.bought_car = []

   def buy_car(self, brand):
      if car.available:
         car.buy()
         self.buy_car.append(car)
      else:
         print(f"el coche {self.brand} no está disponible")

car1 = car("toyota", "chr")
car2 = car("seat", "ibiza")

user1 = user("Bianca", "001")
user2 = user("Marc", "002")

class concesionario:
   def __init__(self):
      self.car = []
      self.user = []

   def add_car(self, car):
        self.car.append(car)
        print(f"El coche {car.brand} ha sido agregado")


   def register_user(self, user):
        self.user.append(user)
        print(f"El usuario {user.name} ha sido registrado")
concesionario = concesionario()
concesionario.add_car(car1)
concesionario.add_car(car2)         

concesionario.register_user(user1)
car1.available = True
user1.buy_car(car1)


      


        