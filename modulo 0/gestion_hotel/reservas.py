from collections import defaultdict
from datetime import datetime

class reserva:
    def __init__(self, nombre_cliente, num_reserva, num_habitacion, checkin, checkout):
        self.nombre_cliente = nombre_cliente
        self.num_reserva = num_reserva
        self.num_habitacion = num_habitacion
        self.checkin = checkin
        self.checkout = checkout

class reservationSystem:
    def __init__(self):
        self.reservas = defaultdict(list)

    def add_reservas(self, reservas):
        self.reservas[reservas.num_habitacion].append(reservas)
        print(f'Reserva creada para {reservas.nombre_cliente} en la habitación {reservas.num_habitacion}')

    def cancel_reserva(self, num_reserva):
        for habitacion, in self.reservas.items():
            for r in reservas:
                if r.num_reserva == num_reserva:
                    reservas.remove(r)
                    print(f"Reserva {num_reserva} cancelada")
                    return
        print('Reserva cancelada.')