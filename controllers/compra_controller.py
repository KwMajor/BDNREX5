from models.compra_model import CompraModel


class CompraController:
    def __init__(self, db):
        self.model = CompraModel(db)

    def criar_compra(self, id_usuario, id_produto, quantidade, valor_total):
        try:
            return self.model.criar(id_usuario, id_produto, quantidade, valor_total)
        except Exception as e:
            return None

    def listar_compras(self):
        try:
            return self.model.listar()
        except Exception as e:
            return []

    def pesquisar_compras(self, termo):
        try:
            return self.model.pesquisar(termo)
        except Exception as e:
            return []

    def buscar_compra(self, id_compra):
        try:
            return self.model.buscar_por_id(id_compra)
        except Exception as e:
            return None
