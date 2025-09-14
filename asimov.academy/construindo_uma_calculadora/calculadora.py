import os;

print("========")

operations = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponenciação"
}

while True:
    os.system("clear");
    i = 0;
    for op, name in operations.items():
        print(i, ":", name);
        i += 1;
    print("\n");
    print("Escolha a operação que deseja realizar:");
    op = int(input());
    op_string = list(operations.keys())[op];
    print("\n")
    print("{} escolhida".format(op_string));
    print("\n")
    print("Qual o primeiro valor?")
    v1 = float(input());
    print("Qual o segundo valor?")
    v2 = float(input());

    if op == 0:
        result = v1 + v2;
    elif op == 1:
        result = v1 - v2;
    elif op == 2:
        result = v1 * v2;
    elif op == 3:
        result = v1 / v2;
    elif op == 4:
        result = v1 ^ v2;

    print("\n")
    print("{} {} {} = {}".format(v1, op_string, v2, result));
    print("\n")
    print("========")

    print("Deseja realizar mais alguma operação?")
    comando = input();
    if comando == 'n':
        break;