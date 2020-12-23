from conexao import conectar
import sqlite3


def atualizarDados(pessoa, nome, preco, quantidade):
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute(f'UPDATE produtos SET nome = "{nome}", preco = "{preco}", quantidade = "{quantidade}"'
                       f' WHERE nome = "{pessoa}"')
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print(e)
