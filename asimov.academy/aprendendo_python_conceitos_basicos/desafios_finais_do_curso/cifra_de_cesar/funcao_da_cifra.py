def gera_cifra(abecedario, caractere, chave_informada):
    pos = abecedario.index(caractere);
    nova_pos = (pos + chave_informada) % 26;
    return abecedario[nova_pos];