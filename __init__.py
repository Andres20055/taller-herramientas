from operations import add, resta, multiplicacion, division, exponente, modulo

def juego():
  puntaje = 0
  while True:
    print('======== Menu ========'
          '\n1. add'
          '\n2. resta'
          '\n3. multiplicacion'
          '\n4. division'
          '\n5. exponente'
          '\n6. modulo'
          '\n0. Salir')
    opcion = int(input('\nElija una opcion: '))

    if opcion == 0:
        break
    numero1 = input('Digite el primer numero: ')
    numero2 = input('Digite el segundo numero: ')
    respuesta = int(input('Digite su respuesta: '))
    
    if opcion == 1:
        resultado = add(numero1, numero2)
        if resultado == respuesta:
            puntaje += 1
            print('Correcto!!')
        else:
            print('Incorrecto')

    if opcion == 2:
        resultado = resta(numero1, numero2)
        if resultado == respuesta:
            puntaje += 1
            print('Correcto!!')
        else:
            print('Incorrecto')

    if opcion == 3:
        resultado = multiplicacion(numero1, numero2)
        if resultado == respuesta:
            puntaje += 2
            print('Correcto!!')
        else:
            print('Incorrecto')

    if opcion == 4:
        resultado = division(numero1, numero2)
        if resultado == respuesta:
            puntaje += 2
            print('Correcto!!')
        else:
            print('Incorrecto')

    if opcion == 5:
        resultado = exponente(numero1, numero2)
        if resultado == respuesta:
            puntaje += 4
            print('Correcto!!')
        else:
            print('Incorrecto')

    if opcion == 6:
        resultado = modulo(numero1, numero2)
        if resultado == respuesta:
            puntaje += 4
            print('Correcto!!')
        else:
            print('Incorrecto')
print(f'======== Game Over ========'
      f'\nTu puntaje es:  {puntaje}'
      '\nSigue intentando!')

Juego()
