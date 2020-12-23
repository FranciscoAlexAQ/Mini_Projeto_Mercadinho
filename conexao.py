import sqlite3
import os


def conectar():
    global connect
    try:
        connect = sqlite3.connect(os.path.dirname(__file__) + '\\mercadinho.db')
    except sqlite3.Error as e:
        print(e)
    return connect


def criarTabela():
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute('CREATE TABLE produtos'
                       '(nome VARCHAR NOT NULL, '
                       'preco VARCHAR NOT NULL,'
                       'quantidade VARCHAR NOT NULL)')
        con.close()
    except sqlite3.Error as e:
        print(e)


def deletarTabela():
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute('DROP TABLE produtos')
        con.close()
    except sqlite3.Error as e:
        print(e)
