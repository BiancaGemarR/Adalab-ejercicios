class Habitaciones:
    def __init__(self, num_habitacion, tipo_habitacion, precio):
        self.num_habitacion = num_habitacion
        self.tipo_habitacion = tipo_habitacion
        self.precio = precio

class ManagementHabitaciones:
    def __init__(self):
        self.habitaciones = {}

    def add_habitacion(self, habitacion):
        self.habitacion[habitacion.num_habitacion] = habitacion
        print(f'La habitación {habitacion.num_habitacion} ha sido agregada')        
    
    def check_disponibilidad(self, num_habitacion):
        habitacion = self.habitacion.get(num_habitacion)
        if habitacion in habitacion.available:
            print(f'La habitacion {num_habitacion} está disponible.')
            return True
        print(f'La habitación {num_habitacion} no está disponible.')
        return False

