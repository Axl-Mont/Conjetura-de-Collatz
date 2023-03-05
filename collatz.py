def collatz(numerSelect):
        cont = 0
        while numerSelect != 1:
                if numerSelect % 2 == 0:
                        numerSelect = int(numerSelect / 2)
                elif numerSelect % 2 != 0:
                        numerSelect = int(numerSelect * 3 + 1)
                cont += 1
                print(f'Numero: {numerSelect}')
        print(f'cantidad de interaciones : {cont}')
number = int(input('Ingresa un numero entero positivo'))
collatz(number)