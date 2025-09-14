numero_secreto = 2;
chances = 3;
descobriu = False;

while chances > 0:
    palpite_do_usuario = int(input('Qual você acha que é o número secreto?'));
    
    if palpite_do_usuario == numero_secreto:
        print('Parabéns, você acertou o número secreto');
        break;
    chances -= 1;
    if palpite_do_usuario < numero_secreto:
         print('O número que você escolheu é menor do que o número secreto.');
    else:
         print('O número que você escolheu é maior do que o número secreto.');

    if chances > 0:
         print(f'Você ainda possui {chances} chances!');

if chances == 0:
    print(f'Infelizmente as suas chances acabaram! O número era {numero_secreto}');