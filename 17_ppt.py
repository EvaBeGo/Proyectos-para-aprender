import random
def rock_paper_scissors():
    wins = 0
    defeats = 0
    ties = 0
    while True:
        opciones = ['piedra', 'papel', 'tijeras']
        pc_option = random.choice(opciones)
        human_option = str(input('✂️ Escribe piedra papel o tijeras 🗿: '))
        if human_option not in (opciones):
            print('❌ Esa opcion no es valida, intentalo de nuevo!')
            continue
        print(f'🖥️ Boniato ha sacado {pc_option}🖥️')
        if human_option == pc_option:
            print('Habeis empatado ☘️')
            ties += 1
        elif human_option == 'piedra' and pc_option == 'tijeras' or \
            human_option == 'tijeras' and pc_option == 'papel' or \
            human_option == 'papel' and pc_option == 'piedra':
            print('🎊 Has ganado! 🎊')
            wins += 1
        else:
            print('Has perdido 💀')
            defeats += 1
        while True:
            seguir = str(input('Quieres continuar jugando? s/n: ')).strip()
            print(f'He recibido: [{seguir}]')
            if seguir == 's' or seguir == 'n':
                break
            print('Por favor, introduce una opcion valida')
        if seguir == 'n':
            print(f'Resultado final - Victorias: {wins}, Derrotas: {defeats}, Empates: {ties}')
            break
rock_paper_scissors()

