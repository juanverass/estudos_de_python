import random

# Função para gerar o baralho 
def gerar_baralho(qtd_baralhos=1, incluir_coringa=False, embaralhar=True):
    naipes = ['♥️', '♦️', '♣️', '♠️']  # Copas, Ouros, Paus, Espadas
    valores = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
    
    baralho = []
    for _ in range(qtd_baralhos):
        for naipe in naipes:
            for valor in valores:
                baralho.append(f'{valor}{naipe}')
        if incluir_coringa:
            baralho.append('🃏 Coringa')
            baralho.append('🃏 Coringa')

    if embaralhar:
        random.shuffle(baralho)

    return baralho

# Função para mostrar o baralho 

def mostrar_baralho(baralho):
    print(f'\nBaralho com {len(baralho)} cartas:')
    print(', '.join(baralho))

# Função para dar as cartas 
    
def dar_as_cartas(baralho, qtd_jogadores, cartas_por_jogador):
    jogadores = [[] for _ in range(qtd_jogadores)]

    for i in range(cartas_por_jogador):
        for j in range(qtd_jogadores):
            if baralho:  # se ainda tem cartas no baralho
                jogadores[j].append(baralho.pop(0))

    return jogadores 

# Função para mostrar jogadores 
def mostrar_jogadores(jogadores):
    for i, mao in enumerate(jogadores, start=1):
        print(f'\nJogador {i} ({len(mao)} cartas): {", ".join(mao)}')

