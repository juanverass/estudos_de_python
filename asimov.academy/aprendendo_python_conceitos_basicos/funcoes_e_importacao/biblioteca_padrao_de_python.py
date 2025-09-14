import math;

print(math.pi);

print(math.log(16,2));

import datetime;

print(datetime.datetime.now());

agora = datetime.datetime.now();

ano_2000 = datetime.datetime(2000, 1, 1);

print(agora - ano_2000);

import random;

for _ in range(5):
    n = random.randint(1,10);
    print(f'Número escolhido: {n}');

nomes = ['Juan', 'Larissa', 'Leonardo'];
for _ in range(5):
    nome = random.choice(nomes);
    print(f'Nome escolhido: {nome}');

import os;

print(os.getcwd());
print(os.listdir());

import time;
funcoes_da_biblioteca = dir(time);
print(funcoes_da_biblioteca);

inicio = time.time();

print('Primeira linha');

time.sleep(3)

print('Segunda linha');

final = time.time();

tempo_execucao = final = inicio;
print(f'O script levou {tempo_execucao:.3f} segundos para executar.');