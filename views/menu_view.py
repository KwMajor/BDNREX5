class MenuView:
    @staticmethod
    def mostrar_menu_principal():
        print("\n=== SISTEMA DE E-COMMERCE ===")
        print("1. Gerenciar Usuarios")
        print("2. Gerenciar Vendedores")
        print("3. Gerenciar Produtos")
        print("4. Gerenciar Compras")
        print("0. Sair")
        return input("Escolha uma opcao: ")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(mensagem)
