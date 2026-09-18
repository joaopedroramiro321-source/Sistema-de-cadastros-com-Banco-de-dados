from cadastros import Cadastro

cad = Cadastro('', '', '')

escolha = 0

print('''
=============================
SISTEMA DE CADASTROS INICIADO
=============================
''')

cad.criar_banco()

while escolha == 0 or escolha == 1 or escolha == 2:

    print('''
    MENU:
        Cadastrar novo usuário   (1)
        Ver usuários cadastrados (2)
        Encerrar                 (3)
    ''')

    escolha = int(input('Informe o que deseja fazer: '))

    if escolha == 1:
        cad.cadastrar('','','')

    elif escolha == 2:
        cad.ver_registros()

    elif escolha == 3:
        break
