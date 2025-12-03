from models.produto_model import ProdutoModel


class ProdutoController:
    def __init__(self, db):
        self.model = ProdutoModel(db)

    def criar_produto(self, nome, descricao, preco, estoque, id_vendedor):
        try:
            return self.model.criar(nome, descricao, preco, estoque, id_vendedor)
        except Exception as e:
            return None

    def editar_produto(self, id_produto, nome=None, descricao=None, preco=None, estoque=None):
        try:
            return self.model.editar(id_produto, nome, descricao, preco, estoque)
        except Exception as e:
            return False

    def listar_produtos(self):
        try:
            return self.model.listar()
        except Exception as e:
            return []

    def pesquisar_produtos(self, termo):
        try:
            return self.model.pesquisar(termo)
        except Exception as e:
            return []

    def buscar_produto(self, id_produto):
        try:
            return self.model.buscar_por_id(id_produto)
        except Exception as e:
            return None

    def buscar_produto_por_id(self, id_produto):
        try:
            return self.model.buscar_por_id(id_produto)
        except Exception as e:
            return None
