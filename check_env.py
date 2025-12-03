from dotenv import load_dotenv
import os

load_dotenv()

print("=== CONFIGURACOES CARREGADAS ===")
print(f"URI: {os.getenv('NEO4J_URI')}")
print(f"Username: {os.getenv('NEO4J_USERNAME')}")
print(f"Password: {'*' * 20 if os.getenv('NEO4J_PASSWORD') else 'NAO DEFINIDA'}")
print(f"Database: {os.getenv('NEO4J_DATABASE')}")
