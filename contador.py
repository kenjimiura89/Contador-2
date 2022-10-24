#2. Crie de forma recursiva uma função que printe do número recebido até o zero.#

from mimetypes import init
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if i < f:
        cont=1
        while cont <=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont+= p
        print('Fim')
    else:
        cont = i 
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim')

contador(1, 10, 1)
contador(10, 0, 2)
print('Selecione a contagem desejada!')
init = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passos: '))
contador(init, fim, pas)