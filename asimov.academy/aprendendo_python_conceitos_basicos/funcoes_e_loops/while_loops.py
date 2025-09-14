# n = 0

# while n < 10:
#     print(f'O valor de n é: {n}')
#     n += 1
#     if n == 5:
#         break;

# for n in range(-5, 6):
#     print(n)
#     if n == 0:
#         continue;
#     resultado = 1/n
#     print(f'O resultado é: {resultado}')

# print('O loop acabou')

# while True:
#     entrada = input('Digite qualquer coisa ("q" para sair): ')
#     print(f'O valor digitado foi: {entrada}')
#     if entrada == "q":
#         break;
# print('Programa finalizado');

while True:
    opt = input('Escolha uma opção (1, 2) | ("q" para sair): ')
    if opt == 'q':
        break
    elif opt != '1' and '2':
        print('Opção inválida!')
        continue;
    print(f'Opção selecionada: {opt}')
print('Programa finalizado');