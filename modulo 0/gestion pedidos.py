from collections import defaultdict
def count_products(orders: list[str]) -> defaultdict:
    #crea un diccionario con valor por defecto 0
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] +=1
    return product_count
    
orders = ['laptop', 'smartphone', 'laptop', 'tablet', 'iphone', 'computer', 'tv', 'speaker', 'computer','tv']
count = count_products(orders)
print(count)

#contar ventas
from collections import Counter
def count_sales(products: list[str]) -> Counter:
    return Counter(products)

sales = ["laptop", "smartphone", "smartphone", "laptop", "tablet"]
result = count_sales(sales)
print(result)

from collections import deque
def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    return delivery_queue
    
queue = manage_delivery_queue()
print(queue)

from enum import Enum
class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

def check_order_status(status: OrderStatus):
    if status == OrderStatus.PENDING:        
        return "El pedido està pendiente de confirmación"
    elif status == OrderStatus.SHIPPED:
        return "El pedido ha salido del almacén"
    elif status == OrderStatus.DELIVERED:
        return "El pedido ha sido entregado"
    
print(check_order_status(OrderStatus.PENDING)) 