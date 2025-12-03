from database import Database
import uuid


class ProdutoModel:
    def __init__(self, db):
        self.db = db

    def criar(self, nome, descricao, preco, estoque, id_vendedor):
        query = """
        MATCH (v:Vendedor {id: $id_vendedor})
        CREATE (p:Produto {id: $id, nome: $nome, descricao: $descricao, preco: $preco, estoque: $estoque})
        CREATE (v)-[:VENDE]->(p)
        RETURN p
        """
        params = {
            'id': str(uuid.uuid4()),
            'nome': nome,
            'descricao': descricao,
            'preco': preco,
            'estoque': estoque,
            'id_vendedor': id_vendedor
        }
        result = self.db.execute_write(query, params)
        return result['p'] if result else None

    def editar(self, id_produto, nome=None, descricao=None, preco=None, estoque=None):
        updates = []
        params = {'id': id_produto}
        
        if nome:
            updates.append("p.nome = $nome")
            params['nome'] = nome
        if descricao:
            updates.append("p.descricao = $descricao")
            params['descricao'] = descricao
        if preco is not None:
            updates.append("p.preco = $preco")
            params['preco'] = preco
        if estoque is not None:
            updates.append("p.estoque = $estoque")
            params['estoque'] = estoque
        
        if not updates:
            return False
        
        query = f"""
        MATCH (p:Produto {{id: $id}})
        SET {', '.join(updates)}
        RETURN p
        """
        result = self.db.execute_write(query, params)
        return result is not None

    def listar(self):
        query = "MATCH (p:Produto) RETURN p"
        results = self.db.execute_query(query)
        return [record['p'] for record in results]

    def pesquisar(self, termo):
        query = """
        MATCH (p:Produto)
        WHERE p.nome CONTAINS $termo OR p.descricao CONTAINS $termo
        RETURN p
        """
        results = self.db.execute_query(query, {'termo': termo})
        return [record['p'] for record in results]

    def buscar_por_id(self, id_produto):
        query = """
        MATCH (p:Produto {id: $id})
        RETURN p
        """
        results = self.db.execute_query(query, {'id': id_produto})
        return results[0]['p'] if results else None
