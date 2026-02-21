import unittest
from unittest.mock import MagicMock
from controllers.usuario_controller import UsuarioController

class TestUsuarioController(unittest.TestCase):
    def setUp(self):
        # Criamos um "mock" (simulador) da classe Database
        self.mock_db = MagicMock()
        # Injetamos o mock no controller
        self.controller = UsuarioController(self.mock_db)

    def test_criar_usuario_sucesso(self):
        # Simulamos o retorno esperado do método execute_write no Model
        # O model retorna result['u']
        self.mock_db.execute_write.return_value = {
            'u': {'nome': 'Teste', 'email': 'teste@email.com', 'id': '123'}
        }

        resultado = self.controller.criar_usuario("Teste", "teste@email.com", "123456789")

        # Verificações
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado['nome'], "Teste")
        self.assertTrue(self.mock_db.execute_write.called)

    def test_buscar_usuario_inexistente(self):
        # Simulamos que execute_query não encontrou nada (lista vazia)
        self.mock_db.execute_query.return_value = []

        resultado = self.controller.buscar_usuario("id-qualquer")

        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()