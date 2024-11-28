from produto import SistemaCadastro

sistemacadastro = SistemaCadastro()
opcao = 0
while opcao != 5:
    print('-' * 30)
    print('Bem vindo ao sistema de estoque!\n')
    print('1. Cadastrar Produto\n2. Listar Produto\n3. Atualizar Produto\n4. Deletar Produto\n5. Sair\n')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        sistemacadastro.cadastrarProduto()
    elif opcao == 2:
        sistemacadastro.listarProduto()
    elif opcao == 3:
        sistemacadastro.atualizarProduto()
    elif opcao == 4:
        sistemacadastro.deletarProduto()
    elif opcao == 5:
        print('Ações finalizadas!\n')
    else:
        print('Opção inválida!')
    