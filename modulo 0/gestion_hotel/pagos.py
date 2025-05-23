import asyncio
import random
import clientes

async def procesar_pago(cliente, cantidad):
    print(f'Procesando pago del cliente {cliente}')
    await asyncio.sleep(random.randint(1,3))
    print(f'Pago procesado del cliente {cliente} con la cantidad {cantidad}€')
    return True
