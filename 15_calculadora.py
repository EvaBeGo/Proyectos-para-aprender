import math               # Importamos matematicas para poder mejorar la calculadora y hacer mas operaciones

def calculator():         
    while True:
        operacion = str(input('Introduce que tipo de operacion quieres hacer, ej: +, -, /, *: '))
        resultado = None

        try:
            numero1 = float(input('introducie el primer numero: '))
            if operacion != 'sqrt':
                numero2 = float(input('introducie el segundo numero: '))
            else:
                numero2 = None

        except ValueError:
            print('❌ Eso no es un numero, intentalo de nuevo.')
            continue


        if operacion == "+":
            resultado = numero1 + numero2
        elif operacion == "-":
            resultado = numero1 - numero2
        elif operacion == '*':
            resultado = numero1 * numero2
        elif operacion == '/':
            if numero2 == 0:
                print('Error: no se puede dividir entre 0')
            else: resultado = numero1 / numero2
        elif operacion == '**':
            resultado = numero1 ** numero2
        elif operacion == 'sqrt':
            if numero1 < 0:
                print('❌ No existe la raiz cuadrada de un numero negativo.')
            else:
                resultado = math.sqrt(numero1)
        else:
            print('❌ Operacion no valida') 
            continue

        print(f'resultado: {resultado}')  

        with open('historial.txt', 'a'):
            if resultado is not None:
                with open('historial.txt', 'a') as f:
                    f.write(f'{numero1} {operacion} {numero2} = {resultado}\n')

        seguir = input('Otra operacion?  (s/n): ')
        if seguir == 'n':
                break
        
calculator()



