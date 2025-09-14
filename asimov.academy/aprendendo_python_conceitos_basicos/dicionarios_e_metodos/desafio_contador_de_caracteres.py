vogais = ['a', 'e', 'i', 'o', 'u']
texto = """
Python é uma linguagem de programação de alto nível,[10] interpretada de
script, imperativa, orientada a objetos, funcional, de tipagem dinâmica
e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui
um modelo de desenvolvimento comunitário, aberto e gerenciado pela
organização sem fins lucrativos Python Software Foundation. Apesar de
várias partes da linguagem possuírem padrões e especificações formais,
a linguagem, como um todo, não é formalmente especificada. O padrão na
pratica é a implementação CPython.
"""
for vogal in vogais:
    quantidade = texto.lower().count(vogal)
    print(f"Existem {quantidade} de {vogal.upper()} no texto.")
    