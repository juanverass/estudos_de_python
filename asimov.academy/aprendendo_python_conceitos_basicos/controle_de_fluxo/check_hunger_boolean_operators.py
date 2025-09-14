print('----- INÍCIO -----\n')

tenhoFome = input('Estou com fome? (Digite s para sim)') == 's';
tenhoComida = input('Tenho comida em casa? (Digite s para sim)') == 's';
 
if tenhoFome and not tenhoComida:
    print('Ir ao mercado')
    print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')

elif tenhoFome and tenhoComida: 
    print('Preparar uma refeição')
    print('Comer a comida')

print('\n----- FIM -----')