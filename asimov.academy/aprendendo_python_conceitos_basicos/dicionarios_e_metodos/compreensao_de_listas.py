valores = list(range(10))
print (f'Nossa lista contem os valores: {valores}')

maiores_que_cinco = []
for valor in valores:
        if valor > 5:
            maiores_que_cinco.append(valor)
print(f'Os numeros da lista, maiores que 5 são: {maiores_que_cinco}')

#Outra forma de tratar a lista
outra_forma_de_maiores_que_cinco = [
    valor
    for valor in valores 
    if valor > 5
]
print(f',Podemos tratar dessa forma também, Os numeros da lista maiores que 5: {outra_forma_de_maiores_que_cinco}')