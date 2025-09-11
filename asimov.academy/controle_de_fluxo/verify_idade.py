idade = int(input('Digite a sua idade: '));

if idade < 18:
    print('Você é menor de idade');
    print('Você não pode dirigir um carro');
elif idade == 18:
    print('Você tem exatamente 18 anos!');
else:
    print('Você tem mais de 18 anos.');