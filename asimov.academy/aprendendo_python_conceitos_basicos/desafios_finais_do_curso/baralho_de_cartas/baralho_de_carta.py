#Baralho de cartas
#Gerar o baralho e exibi-lo
#Dar as cartas para os jogadores
#Exibir o baralho após as cartas terem sido distribuídas
#Exibir a mão de cada jogador
#Funções:
#gerar_baralho - Retorna o baralho, deve definir quantos baralhos devem ter dentro deste baralho se o baralho deve ter coringas e se deve ser embaralhado antes de ser retornado.
#mostrar_baralho - Exibir quantidade de cartas no baralho e quais são.
#dar_as_cartas - distribuir cartas do baralho entre x jogadores e cada jogador deve ter Y cartas
#mostrar_jogadores - Exibe a quantidade de cartas na mão de cada jogador e mostra quais são.
#OBS: Ordem dos naipes: Copas, Ouros, Paus e Espadas. Ás A, 2 à 10, Valete J, Dama Q e Rei K

import funcoes_do_bralho as funcao;

baralho = funcao.gerar_baralho(qtd_baralhos=1, incluir_coringa=False, embaralhar=True)
funcao.mostrar_baralho(baralho)

jogadores = funcao.dar_as_cartas(baralho, qtd_jogadores=4, cartas_por_jogador=5)

print("\n--- Distribuido! ---")
funcao.mostrar_baralho(baralho)
funcao.mostrar_jogadores(jogadores)
