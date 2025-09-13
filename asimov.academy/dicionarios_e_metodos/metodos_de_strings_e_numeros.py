# Escreva o seu código aqui :-)
x = 4.5
x.as_integer_ratio()

print(x)
print(x.as_integer_ratio())

x = 4.5
print(x.is_integer())
x = 4.0
print(x.is_integer())

palavra = 'Olá, Mundo!'
print(palavra)

print(palavra.upper())
print(palavra.lower())

arquivo = '2023_01_01_NotaFiscal.pdf'

print(arquivo)

print(arquivo.endswith('.pdf'))

print(arquivo.startswith('2023'))
print(arquivo.startswith('2024'))

if arquivo.startswith('2023') and arquivo.endswith('.pdf'):
    print('Nota fiscal encontrada!')

texto = 'Hoje em dia o dia é muito dia! Bom Dia!!!!'
print(texto.count('dia'))
print(texto.lower().count('dia'))

seq = 'aaaaabbbaaabbbabababdddd'

print(seq.find('b'))
print(seq.index('b'))


print(seq.find('c'))
#print(seq.index('c')) Gera um erro

print(seq[seq.find('b'):])

s1 = '7834920843920'
print(s1)
print(s1.isdigit())


s2 = 'jhdajkshfdjsfhjkshfjds'
print(s2)
print(s2.isdigit())

s3 = 'Olá 2023 Python!!!'
print(s3)
print(s3.isdigit())

frase = 'Estou estudando Python!!!'
print(frase)
print(frase.replace('!!!','??'))
print(frase.replace('Python', 'Javascript'))

linha = 'Item1   Item2   Item3'
print(linha)
print(linha.split())


linha = 'Item1;Item2;Item3'
print(linha)
print(linha.split(';'))

nomes = ['Joana', 'Marcelo', 'Paulo']
print(nomes)
print('-----'.join(nomes))
print(';'.join(nomes))