def somar_dois(n):
    return n + 2

x = 10
resultado = somar_dois(x)
print(f'O resultado é {resultado}')


def adicionar_final(texto,final='!!!!'):
    return texto + final

print(adicionar_final('Olá'))

def dividir(a,b):
    if b == 0:
        return 'Impossível dividir!!'
    return a/b

print(dividir(10,5))

def dividir(c=0,d=0):
    if d == 0:
        return 'Impossível dividir!!'
    return int(c)/int(d)

c = input('Informe um valor para c: ')
d = input('Informe um valor para d: ')

print(dividir(c,d))

def dizer_ola():
    print('Olá')

dizer_ola()
dizer_ola()