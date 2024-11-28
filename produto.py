class Produto:
    def __init__(self, _nome, _preco, _quantidade, _codigo_produto, _categoria, _preco_total):
        self.nome = _nome
        self.preco = _preco
        self.quantidade = _quantidade
        self.codigo_produto = _codigo_produto
        self.categoria = _categoria
        self.preco_total = _preco_total

class SistemaCadastro:
    def __init__(self):
        self.produtos = []
    
    def cadastrarProduto(self):
        nome = input('Qual o nome do Produto? ')
        preco = float(input('Qual o preço do Produto? '))
        quantidade = int(input('Qual a quantidade do Produto? '))
        codigo_produto = int(input('Qual o codigo do Produto? '))
        categoria = input('Qual a categoria do Produto? ')
        preco_total = preco * quantidade
        produto = Produto(nome, preco, quantidade, codigo_produto, categoria, preco_total)
        self.produtos.append(produto)
    
    def listarProduto(self):
        if not self.produtos:
            print('Nenhum produto cadastrado.\n')
            return

        for produto in self.produtos:
            print('-' * 30)
            print(f'Nome: {produto.nome}')
            print(f'Preço: {produto.preco}')
            print(f'Quantidade: {produto.quantidade}')
            print(f'Código do Produto: {produto.codigo_produto}')
            print(f'Categoria: {produto.categoria}')
            print(f'Preço Total: {produto.preco_total}')
            print('Produto listado com sucesso!')
            print('-' * 30)
    
    def atualizarProduto(self):
        if not self.produtos:
            print('Nenhum produto cadastrado.\n')
            return
        
        codigo = int(input('Qual o código do produto que você deseja atualizar? '))
        for produto in self.produtos:
            if produto.codigo_produto == codigo:
                opcao = 0
                while opcao != 6:
                    print('Escolha uma opção:\n')
                    print('O que você quer atualizar?\n1. Nome\n2. Preço\n3. Quantidade\n4. Código\n5. Categoria\n6. Sair')
                    opcao = int(input('Opção: '))
                    if opcao == 1:
                        self.new_nome = input('Qual o novo nome? ')
                        produto.nome = self.new_nome
                    if opcao == 2:
                        self.new_preco = float(input('Qual o novo preço? '))
                        produto.preco = self.new_preco
                        produto.preco_total = produto.preco * produto.quantidade
                    if opcao == 3:
                        self.new_quantidade = int(input('Qual a nova quantidade? '))
                        produto.quantidade = self.new_quantidade
                        produto.preco_total = produto.preco * produto.quantidade
                    if opcao == 4:
                        self.new_codigo = int(input('Qual o novo codigo? '))
                        produto.codigo_produto = self.new_codigo
                    if opcao == 5:
                        self.new_categoria = input('Qual a nova categoria? ')
                        produto.categoria = self.new_categoria
                    if opcao == 6:
                        print('Produto atualizado!\n')
                        return
        print('Produto não encontrado. Verifique o código e tente novamente.')
    
    def deletarProduto(self):
        if not self.produtos:
            print("Produto nao cadastradado")
            return
        codigo=int(input("Digite o codigo do produto a ser deletado:"))
        for produto in self.produtos:
            if produto.codigo_produto == codigo:
                self.produtos.remove(produto)
                print("Produto deletado")
                return
        print("Produto nao encontrado.Verfique o codigo cadastrado")
            