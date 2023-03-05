def collatz(numerSelect):
        interac = 0
        while numerSelect != 1:
                
                if numerSelect == 1:
                        print(f'cantidad de iteraciones: {interac} \n numero: {numerSelect}')
                elif numerSelect % 2 == 0:
                        numerSelect = numerSelect / 2
                        interac += 1
                        print(f'cantidad de iteraciones: {interac} \n numero: {numerSelect}')
                elif numerSelect % 2 != 0:
                        numerSelect = numerSelect * 3 + 1
                        interac += 1
                        print(f'cantidad de iteraciones: {interac} \n numero: {numerSelect}')


number = int(input('Ingresa un numero entero positivo'))
collatz(number)