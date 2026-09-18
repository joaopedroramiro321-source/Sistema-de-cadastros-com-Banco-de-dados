import sqlite3 as sql

class Cadastro:
    def __init__(self, nome, email, numero):
        self.__nome = nome
        self.__email = email
        self.__numero = numero

    def criar_banco(self):

        conexao = sql.connect('banco.db')
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

        conexao = sql.connect('banco.db')
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

        conexao = sql.connect('banco.db')
        cursor = conexao.cursor()

        # Ver todos os registros
        cursor.execute("SELECT * FROM usuarios")
        linhas = cursor.fetchall()

        for linha in linhas:
            print(linha)

        conexao.commit()
        conexao.close() 
