import random
jugador_nombre = input("Escribe tu nombre aquí")
print("Bienvenido al juego", jugador_nombre)

jugador1 = input('Escoge tu elemento : Piedra, Papel o Tijera')
print("Has escogido:", jugador1)

elemento = ('Piedra', 'Papel', 'Tijeras')
jugador2 = random.choice(elemento)
print("Elemento ordenador", jugador2)


vida = 3
while vida != 6 and vida != 0:
    jugador2 = random.choice(elemento)
    print(jugador2)
    jugador1 = input('Escoge tu elemento : Piedra, Papel o Tijera')
    print("Has escogido:", jugador1)
    if jugador1 == 'Piedra':
        if jugador2 == 'Tijera':
            vida += 1
            print('Has ganado un punto')
        elif  jugador2 == 'Papel':
            vida -= 1
            print('Has perdido la ronda')
        else:
            print('Has empatado')


    if jugador1 == 'Papel':
        if jugador2 == 'Piedra':
            vida += 1
            print('Has ganado un punto')
        elif jugador2 == 'Tijera':
            vida -= 1
            print('Has perdido la ronda')
        else:
            print('Has empatado')
   
    if jugador1 == 'Tijeras':
        if jugador2 == 'Papel':
            vida += 1
            print('Has ganado un punto')
        elif jugador2 == 'Piedra':
            vida -= 1
            print('Has perdido la ronda')
        else:
            print('Has empatado')
    if vida == 6:
        print("Te has pasado el juego")
    elif vida == 0:
        print("Game over")

    