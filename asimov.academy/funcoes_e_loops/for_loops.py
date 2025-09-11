# for n in range(10):
#     print(f'Mariana conta {n}')

clientes = [
    ('Larissa', 'Plano Premium', 'larissa@gmail.com'), 
    ('Rayssa', 'Plano Básico', 'Rayssa@gmail.com')
]

for cliente in clientes:
    nome = cliente[0]
    plano = cliente[1]
    email = cliente[2]
    print(f'Cliente: {nome}\n Plano: {plano}\n E-mail: {email}\n\n')

for cliente in clientes:
    nome, plano, email = cliente
    print(f'Cliente: {nome}\n Plano: {plano}\n E-mail: {email}\n\n')

for nome, plano, email in clientes:
    print(f'Cliente: {nome}\n Plano: {plano}\n E-mail: {email}\n\n')