from models.usuario_model import UsuarioModel


class UsuarioController:
    def __init__(self, db):
        self.model = UsuarioModel(db)

    def criar_usuario(self, nome, email, telefone):
        try:
            return self.model.criar(nome, email, telefone)
        except Exception as e:
            return None

    def editar_usuario(self, id_usuario, nome=None, email=None, telefone=None):
        try:
            return self.model.editar(id_usuario, nome, email, telefone)
        except Exception as e:
            return False

    def listar_usuarios(self):
        try:
            return self.model.listar()
        except Exception as e:
            return []

    def pesquisar_usuarios(self, termo):
        try:
            return self.model.pesquisar(termo)
        except Exception as e:
            return []

    def buscar_usuario(self, id_usuario):
        try:
            return self.model.buscar_por_id(id_usuario)
        except Exception as e:
            return None

    def adicionar_favorito(self, id_usuario, id_produto):
        try:
            return self.model.adicionar_favorito(id_usuario, id_produto)
        except Exception as e:
            return False

    def remover_favorito(self, id_usuario, id_produto):
        try:
            return self.model.remover_favorito(id_usuario, id_produto)
        except Exception as e:
            return False

    def listar_favoritos(self, id_usuario):
        try:
            return self.model.listar_favoritos(id_usuario)
        except Exception as e:
            return []
