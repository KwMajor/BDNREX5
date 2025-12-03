from models.vendedor_model import VendedorModel


class VendedorController:
    def __init__(self, db):
        self.model = VendedorModel(db)

    def criar_vendedor(self, nome, email, telefone, cpf):
        try:
            return self.model.criar(nome, email, telefone, cpf)
        except Exception as e:
            return None

    def editar_vendedor(self, id_vendedor, nome=None, email=None, telefone=None, cpf=None):
        try:
            return self.model.editar(id_vendedor, nome, email, telefone, cpf)
        except Exception as e:
            return False

    def listar_vendedores(self):
        try:
            return self.model.listar()
        except Exception as e:
            return []

    def pesquisar_vendedores(self, termo):
        try:
            return self.model.pesquisar(termo)
        except Exception as e:
            return []

    def buscar_vendedor(self, id_vendedor):
        try:
            return self.model.buscar_por_id(id_vendedor)
        except Exception as e:
            return None
