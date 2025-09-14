# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

quantidade_capitais = len(capitais);
acertos = 0;
erros = 0;

for estado in capitais:
    capital_do_estado = capitais[estado];
    capital_informada = input(f'Qual é a capital do {estado}?\nResposta: ');

    if capital_informada.lower() == capitais[estado].lower():
        print(f'Você acertou, a capital do {estado} é {capital_informada}');
        acertos +=1;
    else:
        print(f'Resposta errada, a capital de {estado} é {capital_do_estado}');
        erros +=1;

    encerrar_quiz = input('\nSe deseja encerrar o desafio digite "stop", ou tecle enter para a próxima pergunta: ').lower()
    if encerrar_quiz == 'stop':
        break;

porcentagem_acerto = (acertos/quantidade_capitais)*100;
print(f'Parabéns você acertou {acertos} de {acertos - quantidade_capitais}, uma porcentagem de {porcentagem_acerto}% de acertos');
