# 1. Importamos un modulo que ya viene con Python para generar numeros aleatorios
import random

def random_number_game():
    secret_number = random.randint(1, 100)     # El ordenador elige un número al azar entre 1 y 100      # Radint se utiliza para generar un numero random integer aleatorio, es decir, sin decimales 
    attemps = 0
    guessed = False

    print('☘️ Bienvenido al juego de dados ☘️')
    print('Tengo un numero entre 1 y 100. Puedes adivinar cual es?')
    print('-' * 50)                            # Esto solo imprime una línea separadora bonita

    while not guessed:
        try:                                 # Pedimos el número al usuario.           # input() siempre devuelve texto, así que usamos int() para convertirlo a número
            user_text = input('Introduce un numero: ')   
            user_number = int(user_text)
            attemps += 1                        # Si llegamos aquí, es que escribió un número válido, así que sumamos 1 intento

            if user_number == secret_number:
                print(f'🎊 Felicidades! Has adivinado el numero secreto en {attemps} intentos. 🎊')
                guessed = True                      # Al cambiar a True, el bucle 'while' terminará
            if user_number > 100:
                print ('Debes escribir un numero entre el 1 y el 100, imbecil')

            elif user_number < secret_number:
                print('El numero oculto es mayor. Intentalo de nuevo.')
            else:
                print('El numero oculto es menor. Intentalo de nuevo.')

        except ValueError:                           # 4. Excepciones: ¿Qué pasa si el usuario escribe "hola" en vez de un número?  ## El int() de arriba fallará, pero en vez de romperse, entra aquí:
            print('❌ Error! Por favor, introduce solo numeros enteros.')
        
# Aqui metemos el segundo juegooo
def death_roll():
    print('\n' + '='*40)
    print('🎲 Bienvenido al Death Roll🎲') 
    print('Reglas: Cuando lance un dado el nuevo resultado sera el maximo, quien saque 1 pierde!')

    current_max = 1000

    while True:
        input(f'\n [player] El maximo es {current_max}. Presiona enter para tirar dados...')
        user_roll = random.randint(1, current_max)
        print(f'👍 Has sacado: {user_roll} 💀')
        if user_roll == 1:
            print('💀Has muerto💀')
            break

        current_max = user_roll

        print('\n Turno del boniatoo...')
        machine_roll = random.randint(1, current_max)

        print(f'🖥️ El boniato tira dados y saca: {machine_roll}')        

        if machine_roll == 1:
            print('🎊 El boniato ha sacado 1!, Has ganado! 🎊')
            break

        current_max = machine_roll

# Menu principal
def main_menu():
    while True:
        print('\n' + '='*30)
        print('       🕹️ Minijuegos 🕹️')
        print('='*30)
        print('1. Jugar: Adivina el numero')
        print('2. Jugar: Death Roll')
        print('3. Salir')

        option = input('\nSelecciona una opcion (1-3): ')
        if option == "1":
            random_number_game()
        elif option == '2':
            death_roll()
        elif option == '3':
            print('Adios!!')
            break
        else:
            print('❌ No es una opcion valida, por favor elige del 1 al 3 ❌')

main_menu()



