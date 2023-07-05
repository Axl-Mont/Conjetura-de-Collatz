def collatz(numberSelect):
        cont = 0
        while numberSelect != 1:
                if numberSelect % 2 == 0:
                        numberSelect = numberSelect // 2
                else:
                        numberSelect = numberSelect * 3 + 1
                cont += 1
                print(f'Numero: {numberSelect}')
        print(f'Cantidad de iteraciones para llegar al ciclo 4-2-1: {cont}')
number = int(input('Ingresa un numero entero positivo: '))
collatz(number)
input()