import statistics
import  csv

#leer datos de venta mensuales
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

    sales =  list(monthly_sales.values())
print(sales)

#hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#Hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

#Hallar la moda
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

#Desviacion Estandar
stdev_sales = statistics.stdev(sales)
print(f"La desviaciÃ³n estÃ¡ndar es: {stdev_sales}")

#Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La moda es: {variance_sales}")

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')
