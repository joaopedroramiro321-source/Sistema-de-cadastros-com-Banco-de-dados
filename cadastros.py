import sqlite3 as sql

class Cadastro:
    def __init__(self, nome, email, numero):
        self.__nome = nome
        self.__email = email
        self.__numero = numero

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
        return self.__nome

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email
        return self.__email

    def get_numero(self):
        return self.__numero
    def set_numero(self, numero):
        self.__numero = numero
        return self.__numero

    def criar_banco(self):

        conexao = sql.connect(r'C:\Users\joaoramiro\Desktop\Dev\Meus-Projetos\Portifólio\Cadastros POO\banco.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT,
            numero TEXT
            )
        ''')

        conexao.commit()

    def cadastrar(self, nome, numero, email):

        conexao = sql.connect(r'C:\Users\joaoramiro\Desktop\Dev\Meus-Projetos\Portifólio\Cadastros POO\banco.db')
        cursor = conexao.cursor()

        nome = input('Informe seu nome: ')
        email = input('Informe seu E-mail: ')
        numero = input('Informe seu numero de telefone: ')

        cursor.execute(
            "INSERT INTO usuarios (nome, email, numero) VALUES (?, ?, ?)",
            (f"{nome}", f"{email}", f"{numero}")
        )

        conexao.commit()
        conexao.close()

    def ver_registros(self):

        conexao = sql.connect(r'C:\Users\joaoramiro\Desktop\Dev\Meus-Projetos\Portifólio\Cadastros POO\banco.db')
        cursor = conexao.cursor()

        # Ver todos os registros
        cursor.execute("SELECT * FROM usuarios")
        linhas = cursor.fetchall()

        for linha in linhas:
            print(linha)

        conexao.commit()
        conexao.close() 