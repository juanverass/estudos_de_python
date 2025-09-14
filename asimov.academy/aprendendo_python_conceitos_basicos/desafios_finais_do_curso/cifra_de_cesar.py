# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

abecedario_minusculo = 'abcdefghijklmnopqrstuvwxyz'
abecedario_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

chave_informada = int(input('Digite um número: '))
texto = input('Digite o texto: ')

resultado = ''

for caractere in texto:
    if caractere in abecedario_minusculo:
        pos = abecedario_minusculo.index(caractere)
        nova_pos = (pos + chave_informada) % 26
        resultado += abecedario_minusculo[nova_pos]

    elif caractere in abecedario_maiusculo:
        pos = abecedario_maiusculo.index(caractere)
        nova_pos = (pos + chave_informada) % 26
        resultado += abecedario_maiusculo[nova_pos]

    else:
        # mantém espaços, acentos e pontuação
        resultado += caractere

print('Texto cifrado:', resultado)
