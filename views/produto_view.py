class ProdutoView:
    @staticmethod
    def mostrar_menu():
        print("\n--- PRODUTOS ---")
        print("1. Criar Produto")
        print("2. Editar Produto")
        print("3. Listar Produtos")
        print("0. Voltar")
        return input("Escolha uma opcao: ")

    @staticmethod
    def obter_dados_produto():
        nome = input("Nome: ")
        descricao = input("Descricao: ")
        preco = float(input("Preco: "))
        estoque = int(input("Estoque: "))
        return nome, descricao, preco, estoque

    @staticmethod
    def selecionar_vendedor(vendedores):
        if not vendedores:
            print("\nNenhum vendedor encontrado.")
            return None
        
        print("\nSelecione um vendedor:")
        for i, v in enumerate(vendedores, 1):
            print(f"{i}. ID: {v['id']} | Nome: {v['nome']} | CPF: {v['cpf']}")
        
        try:
            opcao = int(input("\nNumero do vendedor (0 para cancelar): "))
            if opcao == 0:
                return None
            if 1 <= opcao <= len(vendedores):
                return vendedores[opcao - 1]['id']
            else:
                print("Opcao invalida!")
                return None
        except ValueError:
            print("Entrada invalida!")
            return None

    @staticmethod
    def selecionar_produto(produtos):
        if not produtos:
            print("\nNenhum produto encontrado.")
            return None
        
        print("\nSelecione um produto:")
        for i, p in enumerate(produtos, 1):
            print(f"{i}. ID: {p['id']} | Nome: {p['nome']} | Preco: R$ {p['preco']:.2f}")
        
        try:
            opcao = int(input("\nNumero do produto (0 para cancelar): "))
            if opcao == 0:
                return None
            if 1 <= opcao <= len(produtos):
                return produtos[opcao - 1]['id']
            else:
                print("Opcao invalida!")
                return None
        except ValueError:
            print("Entrada invalida!")
            return None

    @staticmethod
    def obter_dados_edicao():
        print("Deixe em branco para nao alterar")
        nome = input("Novo nome: ")
        descricao = input("Nova descricao: ")
        preco_str = input("Novo preco: ")
        estoque_str = input("Novo estoque: ")
        return (
            nome if nome else None,
            descricao if descricao else None,
            float(preco_str) if preco_str else None,
            int(estoque_str) if estoque_str else None
        )

    @staticmethod
    def mostrar_produtos(produtos):
        if not produtos:
            print("\nNenhum produto encontrado.")
            return
        print("\nLista de Produtos:")
        for p in produtos:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Preco: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(mensagem)
