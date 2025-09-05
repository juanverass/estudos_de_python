nome = input('Olá, informe o seu nome\nDigite aqui: ');
idade = input('Agora informe a sua idade\nDigite aqui:'); 

print('-' * 15)
print(f'Olá {nome}, o seu nome tem {len(nome)} letras');
print(f'Daqui a 5 anos você terá {int(idade) + 5} anos de idade');
print('-' * 15)