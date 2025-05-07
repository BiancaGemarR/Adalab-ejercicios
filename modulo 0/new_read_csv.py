import csv

new_product = {
    'name':'Wireless charger',
    'price': 75,
    'quantity': 100,
    'brand' : 'opo',
    'category' : 'Accessories',
    'entry_date' : '30-04-25'
}

with open(products.csv, mode='a', newline='') as file:
    file.write('\n')