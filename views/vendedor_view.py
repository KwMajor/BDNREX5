class VendedorView:
    @staticmethod
    def mostrar_menu():
        print("\n--- VENDEDORES ---")
        print("1. Criar Vendedor")
        print("2. Editar Vendedor")
        print("3. Listar Vendedores")
        print("0. Voltar")
        return input("Escolha uma opcao: ")

    @staticmethod
    def obter_dados_vendedor():
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        return nome, email, telefone, cpf

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
    def obter_dados_edicao():
        print("Deixe em branco para nao alterar")
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        telefone = input("Novo telefone: ")
        cpf = input("Novo CPF: ")
        return nome if nome else None, email if email else None, telefone if telefone else None, cpf if cpf else None

    @staticmethod
    def mostrar_vendedores(vendedores):
        if not vendedores:
            print("\nNenhum vendedor encontrado.")
            return
        print("\nLista de Vendedores:")
        for v in vendedores:
            print(f"ID: {v['id']} | Nome: {v['nome']} | Email: {v['email']} | CPF: {v['cpf']}")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(mensagem)
