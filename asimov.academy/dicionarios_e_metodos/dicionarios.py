# Dicionários
capitais = {
    'Brasil': 'Brasilia', 
    'França': 'Paris', 
    'Japão': 'Tóquio',
}

del capitais['Brasil']

capitais['Inglaterra'] = 'Londres'

for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')
    
print('\n')

d = dict()

d[10] = 'abc'
d['Chave'] = 5
d[3.15] = True

for key in d:
    value = d[key]
    print(f'Chave: {key}, Valor: {value}')