class Product:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.price = args
        self.discount = kwargs

    def show_product(self):
        print (f'Product: {self.name}')
        print (f'Product: {self.price}')
        print (f'Product: {self.discount}')

    """def calcular_total(): #problemas con el descuento
        if self.discount >0:"""
           
           



product1 = Product ('tablet', 500, '15')
product2 = Product('computer', 875, '8')
product3 = Product('smartphone', 1500)

product1.show_product()
product2.show_product()
product3.show_product()

