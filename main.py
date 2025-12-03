from database import Database
from controllers.usuario_controller import UsuarioController
from controllers.vendedor_controller import VendedorController
from controllers.produto_controller import ProdutoController
from controllers.compra_controller import CompraController
from views.menu_view import MenuView
from views.usuario_view import UsuarioView
from views.vendedor_view import VendedorView
from views.produto_view import ProdutoView
from views.compra_view import CompraView


def menu_usuarios(controller, view, produto_controller=None, produto_view=None):
    while True:
        opcao = view.mostrar_menu()
        
        if opcao == "1":
            nome, email, telefone = view.obter_dados_usuario()
            usuario = controller.criar_usuario(nome, email, telefone)
            if usuario:
                view.mostrar_mensagem(f"Usuario criado com sucesso! ID: {usuario['id']}")
            else:
                view.mostrar_mensagem("Erro ao criar usuario.")
            
        elif opcao == "2":
            usuarios = controller.listar_usuarios()
            id_usuario = view.selecionar_usuario(usuarios)
            if id_usuario:
                nome, email, telefone = view.obter_dados_edicao()
                if controller.editar_usuario(id_usuario, nome, email, telefone):
                    view.mostrar_mensagem("Usuario editado com sucesso!")
                else:
                    view.mostrar_mensagem("Erro ao editar usuario.")
            
        elif opcao == "3":
            usuarios = controller.listar_usuarios()
            view.mostrar_usuarios(usuarios)
            
        elif opcao == "4":
            if produto_controller and produto_view:
                menu_favoritos(controller, view, produto_controller, produto_view)
            else:
                view.mostrar_mensagem("Erro: Controladores nao disponiveis.")
            
        elif opcao == "0":
            break


def menu_favoritos(usuario_controller, usuario_view, produto_controller, produto_view):
    usuarios = usuario_controller.listar_usuarios()
    id_usuario = usuario_view.selecionar_usuario(usuarios)
    
    if not id_usuario:
        usuario_view.mostrar_mensagem("Operacao cancelada.")
        return
    
    while True:
        opcao = usuario_view.mostrar_menu_favoritos()
        
        if opcao == "1":
            produtos = produto_controller.listar_produtos()
            id_produto = produto_view.selecionar_produto(produtos)
            if id_produto:
                if usuario_controller.adicionar_favorito(id_usuario, id_produto):
                    usuario_view.mostrar_mensagem("Produto adicionado aos favoritos!")
                else:
                    usuario_view.mostrar_mensagem("Erro ao adicionar produto aos favoritos.")
        
        elif opcao == "2":
            favoritos = usuario_controller.listar_favoritos(id_usuario)
            id_produto = produto_view.selecionar_produto(favoritos)
            if id_produto:
                if usuario_controller.remover_favorito(id_usuario, id_produto):
                    usuario_view.mostrar_mensagem("Produto removido dos favoritos!")
                else:
                    usuario_view.mostrar_mensagem("Erro ao remover produto dos favoritos.")
        
        elif opcao == "3":
            favoritos = usuario_controller.listar_favoritos(id_usuario)
            usuario_view.mostrar_produtos_favoritos(favoritos)
        
        elif opcao == "0":
            break


def menu_vendedores(controller, view):
    while True:
        opcao = view.mostrar_menu()
        
        if opcao == "1":
            nome, email, telefone, cpf = view.obter_dados_vendedor()
            vendedor = controller.criar_vendedor(nome, email, telefone, cpf)
            if vendedor:
                view.mostrar_mensagem(f"Vendedor criado com sucesso! ID: {vendedor['id']}")
            else:
                view.mostrar_mensagem("Erro ao criar vendedor.")
            
        elif opcao == "2":
            vendedores = controller.listar_vendedores()
            id_vendedor = view.selecionar_vendedor(vendedores)
            if id_vendedor:
                nome, email, telefone, cpf = view.obter_dados_edicao()
                if controller.editar_vendedor(id_vendedor, nome, email, telefone, cpf):
                    view.mostrar_mensagem("Vendedor editado com sucesso!")
                else:
                    view.mostrar_mensagem("Erro ao editar vendedor.")
            
        elif opcao == "3":
            vendedores = controller.listar_vendedores()
            view.mostrar_vendedores(vendedores)
            
        elif opcao == "0":
            break


def menu_produtos(controller, view, vendedor_controller, vendedor_view):
    while True:
        opcao = view.mostrar_menu()
        
        if opcao == "1":
            nome, descricao, preco, estoque = view.obter_dados_produto()
            vendedores = vendedor_controller.listar_vendedores()
            id_vendedor = view.selecionar_vendedor(vendedores)
            if id_vendedor:
                produto = controller.criar_produto(nome, descricao, preco, estoque, id_vendedor)
                if produto:
                    view.mostrar_mensagem(f"Produto criado com sucesso! ID: {produto['id']}")
                else:
                    view.mostrar_mensagem("Erro ao criar produto.")
            else:
                view.mostrar_mensagem("Criacao de produto cancelada.")
            
        elif opcao == "2":
            produtos = controller.listar_produtos()
            id_produto = view.selecionar_produto(produtos)
            if id_produto:
                nome, descricao, preco, estoque = view.obter_dados_edicao()
                if controller.editar_produto(id_produto, nome, descricao, preco, estoque):
                    view.mostrar_mensagem("Produto editado com sucesso!")
                else:
                    view.mostrar_mensagem("Erro ao editar produto.")
            
        elif opcao == "3":
            produtos = controller.listar_produtos()
            view.mostrar_produtos(produtos)
            
        elif opcao == "0":
            break


def menu_compras(controller, view, usuario_controller, usuario_view, produto_controller, produto_view):
    while True:
        opcao = view.mostrar_menu()
        
        if opcao == "1":
            usuarios = usuario_controller.listar_usuarios()
            id_usuario = view.selecionar_usuario(usuarios)
            
            if id_usuario:
                produtos = produto_controller.listar_produtos()
                id_produto = view.selecionar_produto(produtos)
                
                if id_produto:
                    quantidade = view.obter_dados_compra()
                    
                    # Buscar informacoes do produto para calcular valor
                    produto = produto_controller.buscar_produto_por_id(id_produto)
                    if produto:
                        valor_total = produto['preco'] * quantidade
                        
                        compra = controller.criar_compra(id_usuario, id_produto, quantidade, valor_total)
                        if compra:
                            view.mostrar_resumo_compra(produto['nome'], quantidade, valor_total)
                            view.mostrar_mensagem(f"\nCompra criada com sucesso! ID: {compra['id']}")
                        else:
                            view.mostrar_mensagem("Erro ao criar compra.")
                    else:
                        view.mostrar_mensagem("Erro: Produto nao encontrado.")
                else:
                    view.mostrar_mensagem("Criacao de compra cancelada.")
            else:
                view.mostrar_mensagem("Criacao de compra cancelada.")
            
        elif opcao == "2":
            compras = controller.listar_compras()
            view.mostrar_compras(compras)
            
        elif opcao == "0":
            break


def main():
    db = Database()
    
    usuario_controller = UsuarioController(db)
    vendedor_controller = VendedorController(db)
    produto_controller = ProdutoController(db)
    compra_controller = CompraController(db)
    
    menu_view = MenuView()
    usuario_view = UsuarioView()
    vendedor_view = VendedorView()
    produto_view = ProdutoView()
    compra_view = CompraView()
    
    try:
        while True:
            opcao = menu_view.mostrar_menu_principal()
            
            if opcao == "1":
                menu_usuarios(usuario_controller, usuario_view, produto_controller, produto_view)
            elif opcao == "2":
                menu_vendedores(vendedor_controller, vendedor_view)
            elif opcao == "3":
                menu_produtos(produto_controller, produto_view, vendedor_controller, vendedor_view)
            elif opcao == "4":
                menu_compras(compra_controller, compra_view, usuario_controller, usuario_view, produto_controller, produto_view)
            elif opcao == "0":
                menu_view.mostrar_mensagem("Saindo...")
                break
            else:
                menu_view.mostrar_mensagem("Opcao invalida!")
    finally:
        db.close()


if __name__ == "__main__":
    main()
