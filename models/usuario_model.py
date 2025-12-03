from database import Database
import uuid


class UsuarioModel:
    def __init__(self, db):
        self.db = db

    def criar(self, nome, email, telefone):
        query = """
        CREATE (u:Usuario {id: $id, nome: $nome, email: $email, telefone: $telefone})
        RETURN u
        """
        params = {
            'id': str(uuid.uuid4()),
            'nome': nome,
            'email': email,
            'telefone': telefone
        }
        result = self.db.execute_write(query, params)
        return result['u'] if result else None

    def editar(self, id_usuario, nome=None, email=None, telefone=None):
        updates = []
        params = {'id': id_usuario}
        
        if nome:
            updates.append("u.nome = $nome")
            params['nome'] = nome
        if email:
            updates.append("u.email = $email")
            params['email'] = email
        if telefone:
            updates.append("u.telefone = $telefone")
            params['telefone'] = telefone
        
        if not updates:
            return False
        
        query = f"""
        MATCH (u:Usuario {{id: $id}})
        SET {', '.join(updates)}
        RETURN u
        """
        result = self.db.execute_write(query, params)
        return result is not None

    def listar(self):
        query = """
        MATCH (u:Usuario)
        OPTIONAL MATCH (u)-[:FAVORITA]->(p:Produto)
        RETURN u, collect(p) as favoritos
        """
        results = self.db.execute_query(query)
        usuarios = []
        for record in results:
            usuario = dict(record['u'])
            # Filtrar produtos None da lista de favoritos
            favoritos = [dict(p) for p in record['favoritos'] if p is not None]
            usuario['favoritos'] = favoritos
            usuarios.append(usuario)
        return usuarios

    def pesquisar(self, termo):
        query = """
        MATCH (u:Usuario)
        WHERE u.nome CONTAINS $termo OR u.email CONTAINS $termo OR u.telefone CONTAINS $termo
        RETURN u
        """
        results = self.db.execute_query(query, {'termo': termo})
        return [record['u'] for record in results]

    def buscar_por_id(self, id_usuario):
        query = """
        MATCH (u:Usuario {id: $id})
        RETURN u
        """
        results = self.db.execute_query(query, {'id': id_usuario})
        return results[0]['u'] if results else None

    def adicionar_favorito(self, id_usuario, id_produto):
        query = """
        MATCH (u:Usuario {id: $id_usuario})
        MATCH (p:Produto {id: $id_produto})
        MERGE (u)-[:FAVORITA]->(p)
        RETURN p
        """
        params = {'id_usuario': id_usuario, 'id_produto': id_produto}
        result = self.db.execute_write(query, params)
        return result is not None

    def remover_favorito(self, id_usuario, id_produto):
        query = """
        MATCH (u:Usuario {id: $id_usuario})-[r:FAVORITA]->(p:Produto {id: $id_produto})
        DELETE r
        RETURN p
        """
        params = {'id_usuario': id_usuario, 'id_produto': id_produto}
        result = self.db.execute_write(query, params)
        return result is not None

    def listar_favoritos(self, id_usuario):
        query = """
        MATCH (u:Usuario {id: $id_usuario})-[:FAVORITA]->(p:Produto)
        RETURN p
        """
        results = self.db.execute_query(query, {'id_usuario': id_usuario})
        return [record['p'] for record in results]
