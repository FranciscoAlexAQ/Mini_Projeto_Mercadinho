import colorama
from listar import listarProdutos
from cadastrar import cadastrarProdutos
from deletar import excluirProdutos
from atualizar import atualizarDados


def exibir():
    print(colorama.Fore.GREEN + 60 * '-' + colorama.Fore.RESET)
    print('{:>50}'.format(colorama.Fore.GREEN + 'MERCADINHO SÃO JOSÉ' + colorama.Fore.RESET))
    print(colorama.Fore.GREEN + 60 * '-' + colorama.Fore.RESET)
    print()
    print('{:>45}'.format(colorama.Fore.LIGHTBLUE_EX + 58 * '*'))
    print('{:>40}'.format('Tabela de produtos'))
    print('{:>40}'.format(58 * '*' + colorama.Fore.RESET))

    print('' + colorama.Style.BRIGHT, colorama.Fore.BLUE)
    print('{:>12}'.format(58 * '-'))
    print('{:>9} {:^30} {:>5}'.format('NOME', 'PREÇO', 'QUANTIDADE'))
    print(58 * '-')


def organizarDadosDoBanco():
    for i in range(len(listarProdutos())):
        print('{:>10} {:>6} {:>6}{:^10} {:>2} {:>5}{:>10} {:>4}'.format(listarProdutos()[i][0], '|',
                        'R$', listarProdutos()[i][1], '|', listarProdutos()[i][2], 'Unidades', '|'))
        print(58 * '-')
    print('' + colorama.Style.RESET_ALL)


def escolhas():
    print('{}'.format(colorama.Fore.YELLOW + 59 * '-'))
    print('{:>50}'.format('Tabela de opções para o administrador: '))
    print('{}'.format(59 * '-'))

    print('{}'.format('-----> DIGITE [1] PARA CADASTRO'))
    print('{}'.format('-----> DIGITE [2] PARA EXCLUIR'))
    print('{}'.format('-----> DIGITE [3] PARA ATUALIZAR'))
    print('{}'.format('-----> DIGITE [4] PARA SAIR'))
    print(59 * '-')

    escolha = int(input(f'DIGITE SUA OPÇÃO: '))
    print('' + colorama.Fore.RESET)

    if escolha == 1:
        cadastro()
        print(4 * '\n')
        main()
    elif escolha == 2:
        delete()
        print(4 * '\n')
        main()
    elif escolha == 3:
        atualizacao()
        print(4 * '\n')
        main()
    else:
        print('Tarefas Salvas com sucesso!')


def cadastro():
    print('Muito bem, vamos lá: ')
    nome = input('Digite o nome do produto que deseja cadastrar: ').title().strip()
    preco = input('Agora digite o preço do produto: ').title().strip()
    quant = input('E por fim, digite sua quantidade: ').title().strip()
    cadastrarProdutos(nome, preco, quant)


def delete():
    print('Muito bem, vamos lá: ')
    nome = input('Digite o nome do produto que deseja excluir: ').title()
    excluirProdutos(nome)


def atualizacao():
    print('Muito bem, vamos lá: ')
    nome = input('Digite o nome do produto que deseja atualizar: ').title()

    nomeMuda = input('Digite o novo nome se deseja mudar o nome. Se não, dê ENTER: ').title()
    if nomeMuda == '':
        for i in range(len(listarProdutos())):
            if nome == listarProdutos()[i][0]:
                nomeMuda = listarProdutos()[i][0]
                break
    precoMuda = input('Digite o novo preço se deseja mudar o preço. Se não, dê ENTER: ').title()
    if precoMuda == '':
        for i in range(len(listarProdutos())):
            if nome == listarProdutos()[i][0]:
                precoMuda = listarProdutos()[i][1]
                break
    quantidadeMuda = input('Digite a nova quantidade se deseja mudar a quantidade. Se não, dê ENTER: ').title()
    if quantidadeMuda == '':
        for i in range(len(listarProdutos())):
            if nome == listarProdutos()[i][0]:
                quantidadeMuda = listarProdutos()[i][2]
                break
    atualizarDados(nome, nomeMuda, precoMuda, quantidadeMuda)


def main():
    exibir()
    organizarDadosDoBanco()
    escolhas()


main()
