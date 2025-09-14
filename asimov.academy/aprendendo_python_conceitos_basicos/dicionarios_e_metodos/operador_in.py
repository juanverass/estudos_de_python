# O operador in

capitais = {
    'Brasil': 'Brasilia', 
    'França': 'Paris', 
    'Japão': 'Tóquio',
}

print('Brasil' in capitais)

pais = 'França'

if pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')
else:
    print(f'Não há capital registrada para o país {pais}')
    
print('\n')
    
    
valores = [1, 2, 3]

val = 4

if val in valores:
    print(val)
else:
    print('N')
    
print('\n')
texto = 'Eu estou estudando Python na Asimov'

txt = 'Eu estou'

if txt in texto:
    print(txt)
else:
    print('N')
    
print('\n')

# in no lugar de and
while True:
    opt = input('Escolha uma opção (1, 2) | "q" para sair: ')
    if opt == 'q':
        break
    elif opt not in ('1', '2'):
        print('Opção inválida!')
        continue
    print(f'Opção selecionada: {opt}')

print('Programa Finalizado')