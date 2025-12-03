from database import Database
from models.usuario_model import UsuarioModel

try:
    db = Database()
    print("Conexao estabelecida com sucesso!")
    
    usuario_model = UsuarioModel(db)
    print("Tentando criar usuario...")
    
    usuario_model.criar("teste1", "João Silva", "joao@email.com", "11999999999")
    print("Usuario criado com sucesso!")
    
    print("\nListando usuarios:")
    usuarios = usuario_model.listar()
    for u in usuarios:
        print(f"- {u}")
    
    db.close()
    print("\nTeste concluido com sucesso!")
    
except Exception as e:
    print(f"Erro: {e}")
    import traceback
    traceback.print_exc()
