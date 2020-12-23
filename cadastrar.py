import sqlite3
from conexao import conectar


def cadastrarProdutos(nome, preco, quantidade):
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute(f'INSERT INTO produtos (rowid, nome, preco, quantidade) VALUES (NULL, "{nome}", '
                       f'"{preco}", "{quantidade}")')
        con.commit()
        con.close()
        print('cadstrado com sucesso')
    except sqlite3.Error as e:
        print(e)
