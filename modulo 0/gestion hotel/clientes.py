class Clientes:
    def __init__(self, name, surname, num_reserva, cantidad):
        self.name = name
        self.surname = surname
        self.num_reserva = num_reserva
        self.cantidad = cantidad

class Managementclientes:
    def __init__(self):
        self.cliente = {}

#agregar cliente al sistema
    # Agregar cliente al sistema
    def add_cliente(self, cliente):
        self.cliente[cliente.num_reserva] = cliente
        print(f'Cliente {cliente.name} ha sido agregado al sistema.')

    # Buscar el cliente por número de reserva
    def get_cliente(self, num_reserva):
        cliente = self.cliente.get(num_reserva)
        if cliente:
            print(f'Cliente encontrado: {cliente.name} {cliente.surname}')
            return cliente
        else:
            print(f'Cliente con número de reserva {num_reserva} no encontrado.')
            return None

#buscar el cliente por número de reserva
  

lista_clientes = Managementclientes()    
cliente_1 = Clientes('Laura', 'ramos', 1, 349)
lista_clientes.add_cliente(cliente_1)
lista_clientes.get_cliente(2)
