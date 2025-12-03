from database import Database


class Vendedor:
    def __init__(self, db):
        self.db = db

    def criar(self, id_vendedor, nome, email, telefone, cpf):
        query = """
        CREATE (v:Vendedor {id: $id, nome: $nome, email: $email, telefone: $telefone, cpf: $cpf})
        RETURN v
        """
        params = {
            'id': id_vendedor,
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'cpf': cpf
        }
        self.db.execute_write(query, params)
        return True

    def editar(self, id_vendedor, nome=None, email=None, telefone=None, cpf=None):
        updates = []
        params = {'id': id_vendedor}
        
        if nome:
            updates.append("v.nome = $nome")
            params['nome'] = nome
        if email:
            updates.append("v.email = $email")
            params['email'] = email
        if telefone:
            updates.append("v.telefone = $telefone")
            params['telefone'] = telefone
        if cpf:
            updates.append("v.cpf = $cpf")
            params['cpf'] = cpf
        
        if not updates:
            return False
        
        query = f"""
        MATCH (v:Vendedor {{id: $id}})
        SET {', '.join(updates)}
        RETURN v
        """
        result = self.db.execute_write(query, params)
        return result is not None

    def listar(self):
        query = "MATCH (v:Vendedor) RETURN v"
        results = self.db.execute_query(query)
        return [record['v'] for record in results]

    def pesquisar(self, termo):
        query = """
        MATCH (v:Vendedor)
        WHERE v.nome CONTAINS $termo OR v.email CONTAINS $termo OR v.cpf CONTAINS $termo
        RETURN v
        """
        results = self.db.execute_query(query, {'termo': termo})
        return [record['v'] for record in results]

    def buscar_por_id(self, id_vendedor):
        query = """
        MATCH (v:Vendedor {id: $id})
        RETURN v
        """
        results = self.db.execute_query(query, {'id': id_vendedor})
        return results[0]['v'] if results else None
