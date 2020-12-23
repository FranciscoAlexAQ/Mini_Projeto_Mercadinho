import sqlite3
from conexao import conectar


def listarProdutos():
    global dados
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM produtos order by nome')
        dados = cursor.fetchall()
        con.close()
    except sqlite3.Error as e:
        print(e)
    return dados
