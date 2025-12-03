from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

print(f"URI: {uri}")
print(f"Usuario: {user}")
print(f"Senha: {'*' * len(password) if password else 'None'}")
print("\nTentando conectar...")

try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
    driver.verify_connectivity()
    print("Conexao verificada com sucesso!")
    
    with driver.session() as session:
        result = session.run("RETURN 1 as num")
        record = result.single()
        print(f"Teste de query: {record['num']}")
    
    driver.close()
    print("Tudo funcionando!")
    
except Exception as e:
    print(f"\nErro de conexao: {e}")
    import traceback
    traceback.print_exc()
