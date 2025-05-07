import random

#generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

#elegir colores aleatorios
colors = ['purpura', 'lavanda', 'lila']
random_color = random.choice(colors)
print(random_color)

#barajar una lista de cartas
cards = ['as', ' rey', 'reina','bastos', 'jota', '9', '10']
random.shuffle(cards)
print(cards)
