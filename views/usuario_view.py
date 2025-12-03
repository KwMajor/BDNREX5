class UsuarioView:
    @staticmethod
    def mostrar_menu():
        print("\n--- USUARIOS ---")
        print("1. Criar Usuario")
        print("2. Editar Usuario")
        print("3. Listar Usuarios")
        print("4. Gerenciar Favoritos")
        print("0. Voltar")
        return input("Escolha uma opcao: ")

    @staticmethod
    def obter_dados_usuario():
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        return nome, email, telefone

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
    def obter_dados_edicao():
        print("Deixe em branco para nao alterar")
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        telefone = input("Novo telefone: ")
        return nome if nome else None, email if email else None, telefone if telefone else None

    @staticmethod
    def mostrar_usuarios(usuarios):
        if not usuarios:
            print("\nNenhum usuario encontrado.")
            return
        print("\nLista de Usuarios:")
        for u in usuarios:
            favoritos = u.get('favoritos', [])
            favoritos_str = ", ".join([f"{p['nome']}" for p in favoritos]) if favoritos else "Nenhum"
            print(f"ID: {u['id']} | Nome: {u['nome']} | Email: {u['email']} | Telefone: {u['telefone']}")
            print(f"  Favoritos: {favoritos_str}")

    @staticmethod
    def mostrar_menu_favoritos():
        print("\n--- FAVORITOS ---")
        print("1. Adicionar Produto aos Favoritos")
        print("2. Remover Produto dos Favoritos")
        print("3. Listar Produtos Favoritos")
        print("0. Voltar")
        return input("Escolha uma opcao: ")

    @staticmethod
    def mostrar_produtos_favoritos(produtos):
        if not produtos:
            print("\nNenhum produto favorito encontrado.")
            return
        print("\nLista de Produtos Favoritos:")
        for p in produtos:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Preco: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(mensagem)
