class CompraView:
    @staticmethod
    def mostrar_menu():
        print("\n--- COMPRAS ---")
        print("1. Criar Compra")
        print("2. Listar Compras")
        print("0. Voltar")
        return input("Escolha uma opcao: ")

    @staticmethod
    def obter_dados_compra():
        quantidade = int(input("Quantidade: "))
        return quantidade

    @staticmethod
    def selecionar_usuario(usuarios):
        if not usuarios:
            print("\nNenhum usuario encontrado.")
            return None
        
        print("\nSelecione um usuario:")
        for i, u in enumerate(usuarios, 1):
            print(f"{i}. ID: {u['id']} | Nome: {u['nome']} | Email: {u['email']}")
        
        try:
            opcao = int(input("\nNumero do usuario (0 para cancelar): "))
            if opcao == 0:
                return None
            if 1 <= opcao <= len(usuarios):
                return usuarios[opcao - 1]['id']
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
            print(f"{i}. ID: {p['id']} | Nome: {p['nome']} | Preco: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")
        
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
    def mostrar_compras(compras):
        if not compras:
            print("\nNenhuma compra encontrada.")
            return
        print("\nLista de Compras:")
        for c in compras:
            print(f"ID: {c['id']} | Usuario: {c['usuario']} | Produto: {c['produto']} | Qtd: {c['quantidade']} | Total: R$ {c['valor_total']:.2f}")

    @staticmethod
    def mostrar_resumo_compra(produto_nome, quantidade, valor_total):
        print(f"\nResumo da Compra:")
        print(f"Produto: {produto_nome}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor Final: R$ {valor_total:.2f}")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(mensagem)
