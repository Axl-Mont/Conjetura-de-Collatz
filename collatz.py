def collatz(numerSelect):
        cont = 0
        while numerSelect != 1:
                if numerSelect % 2 == 0:
                        numerSelect = int(numerSelect / 2)
                else:
                        numerSelect = int(numerSelect * 3 + 1)
                cont += 1
                print(f'Numero: {numerSelect}')
        print(f'Cantidad de iteraciones para llegar al ciclo 4-2-1: {cont}')
number = int(input('Ingresa un numero entero positivo: '))
collatz(number)
input()