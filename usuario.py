from database import Database


class Usuario:
    def __init__(self, db):
        self.db = db

    def criar(self, id_usuario, nome, email, telefone):
        query = """
        CREATE (u:Usuario {id: $id, nome: $nome, email: $email, telefone: $telefone})
        RETURN u
        """
        params = {
            'id': id_usuario,
            'nome': nome,
            'email': email,
            'telefone': telefone
        }
        self.db.execute_write(query, params)
        return True

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
        query = "MATCH (u:Usuario) RETURN u"
        results = self.db.execute_query(query)
        return [record['u'] for record in results]

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
