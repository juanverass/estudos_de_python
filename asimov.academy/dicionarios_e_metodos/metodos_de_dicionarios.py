# Escreva o seu código aqui :-)
produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00,
}
#Métodos e Dicionários
#print(produtos.clear())
print(produtos)

print(produtos.get('banana'))
print(produtos.get('leite'))
print(produtos.get('arroz','Não foi encontrado'))

resultado = produtos.get('banana')

print(resultado)

resultado = produtos.get('arroz')

print(resultado)

print(produtos.setdefault('arroz',9.45))

print(produtos)

for produto in produtos.keys():
    print(produto)

for valor in produtos.values():
    print(valor)

for par in produtos.items():
    print(par)    
    
for k, v in produtos.items():
    print(f'{k} -> {v}')        
    
novos_produtos = {
    'banana': 4.60,
    'massa': 5.90,
    'peixe': 11.90,
    'biscoito': 2.00,
}
print(produtos)
print(novos_produtos)

print(produtos.update(novos_produtos))

print(produtos)

produtos_copia = produtos.copy()

produtos_copia['Morango']= 3.30

print(produtos)

print(produtos_copia)