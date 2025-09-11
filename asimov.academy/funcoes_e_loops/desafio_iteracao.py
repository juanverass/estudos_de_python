# Dado uma sequência de números, calcule a soma e a média dos números.
# ATENÇÃO: não vale usar a função sum()!

sequencia = [2, 5, 7, 16];
soma = 0;
media = 0;

for numero in sequencia:
    soma += numero
media = soma/len(sequencia);
print(f'A soma dos números da lista é igual a {soma}')
print(f'A média dos números da lista é igual a {media}')

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max()!

maior_valor = 0;
for numero in sequencia:
    if numero > maior_valor:
        maior_valor = numero
print(f'O maior número da lista é {maior_valor}')

# Dado uma lista de palavras, printe todas as palavras.
# com pelo menos 5 caracteres
palavras_apenas_palavras = [
    'Juan',
    'Theo',
    'Larissa', 
    'Academia',
    'Futebol',
    'Minecraft'
]

for palavra in palavras_apenas_palavras:
    if len(palavra)  >=5:
        print(palavra);
