from database import Database
from datetime import datetime
import uuid


class CompraModel:
    def __init__(self, db):
        self.db = db

    def criar(self, id_usuario, id_produto, quantidade, valor_total):
        query = """
        MATCH (u:Usuario {id: $id_usuario})
        MATCH (p:Produto {id: $id_produto})
        CREATE (c:Compra {
            id: $id, 
            quantidade: $quantidade, 
            valor_total: $valor_total,
            data: $data
        })
        CREATE (u)-[:REALIZOU]->(c)
        CREATE (c)-[:CONTEM]->(p)
        RETURN c
        """
        params = {
            'id': str(uuid.uuid4()),
            'id_usuario': id_usuario,
            'id_produto': id_produto,
            'quantidade': quantidade,
            'valor_total': valor_total,
            'data': datetime.now().isoformat()
        }
        result = self.db.execute_write(query, params)
        return result['c'] if result else None

    def listar(self):
        query = """
        MATCH (u:Usuario)-[:REALIZOU]->(c:Compra)-[:CONTEM]->(p:Produto)
        RETURN c, u.nome as usuario, p.nome as produto
        """
        results = self.db.execute_query(query)
        compras = []
        for record in results:
            compra = record['c'].copy()
            compra['usuario'] = record['usuario']
            compra['produto'] = record['produto']
            compras.append(compra)
        return compras

    def pesquisar(self, termo):
        query = """
        MATCH (u:Usuario)-[:REALIZOU]->(c:Compra)-[:CONTEM]->(p:Produto)
        WHERE u.nome CONTAINS $termo OR p.nome CONTAINS $termo
        RETURN c, u.nome as usuario, p.nome as produto
        """
        results = self.db.execute_query(query, {'termo': termo})
        compras = []
        for record in results:
            compra = record['c'].copy()
            compra['usuario'] = record['usuario']
            compra['produto'] = record['produto']
            compras.append(compra)
        return compras

    def buscar_por_id(self, id_compra):
        query = """
        MATCH (u:Usuario)-[:REALIZOU]->(c:Compra {id: $id})-[:CONTEM]->(p:Produto)
        RETURN c, u.nome as usuario, p.nome as produto
        """
        results = self.db.execute_query(query, {'id': id_compra})
        if results:
            compra = results[0]['c'].copy()
            compra['usuario'] = results[0]['usuario']
            compra['produto'] = results[0]['produto']
            return compra
        return None
