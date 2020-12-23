import conexao
import sqlite3


def excluirProdutos(valor):
    try:
        con = conexao.conectar()
        cursor = con.cursor()
        cursor.execute(f'DELETE FROM produtos WHERE nome = "{valor}"')
        con.commit()
        con.close()
        print('ok')
    except sqlite3.Error as e:
        print(e)
