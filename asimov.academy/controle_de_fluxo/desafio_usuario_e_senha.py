usuario_correto = 'juan.veras'
senha_correta = 'teste123'

user = input('Informe o Usuário\nUsuário: ');
password = input('Agora informe a senha\nSenha: ');

if user == usuario_correto and password == senha_correta:
    print(f'Olá {user}, você esta conectado(a)');
elif user != usuario_correto:
    print('Usuário inválido!');
elif password != senha_correta:
    print('Senha inválida!');