# Escreva o seu código aqui :-)

#Tuplas
tup = (0,0,0,1,0,1,0)

print(tup.index(1))
print(tup.count(0))

#Listas
l1 = [0,0,0,1,0,1,0]
print(l1)

l2 = l1.copy()
print(l2)

l1.clear()
print(l1)

for n in range(5):
    l1.append(n *2)
print(l1)

valores = [10, 30, -90, -1, 0, 1]
valores_positivos = []

for valor in valores:
    if valor > 0:
        valores_positivos.append(valor)
print(f'Esses são os valores positivos: {valores_positivos}')
    

valores_negativos = []
for valor in valores:
    if valor < 0:
        valores_negativos.append(valor)
print(f'Esses são os valores negativos: {valores_negativos}')


numeros = [1,2,3]
print(numeros)

numeros.append([4,5,6])
print(numeros)

numeros.clear()

numeros = [1,2,3]
print(numeros)

numeros.extend([4,5,6])
print(numeros)

numeros.clear()

numeros=[1,2,3]
novos_numeros = numeros + [4,5,6,7]
print(novos_numeros)

vogais = ['a','i','o','u']
print(vogais)

vogais.insert(1,'e')
print(vogais)

valores.clear()

valores = [150,20,30,40,50]
print(valores)

valor_removido = valores.pop()
print(valor_removido)

vogais.insert(10000,'e')
print(vogais)

vogais.insert(-10000,'e')
print(vogais)

vogal_removido = vogais.pop()
print(vogal_removido)
print(vogais)

vogal_removido = vogais.pop(0)
print(vogal_removido)
print(vogais)

clientes = ['aaa','sss','ddd']
print(clientes)
while clientes:
    cliente = clientes.pop()
    print(f'Processando cliente: {cliente}')
print(clientes)

print(valores)
valores.reverse()
print(valores)

valores = valores + [10,50,60,70]

valores.sort()
print(valores)
valores.reverse()
print(valores)