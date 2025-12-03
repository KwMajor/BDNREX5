# Sistema de E-commerce com Neo4j

Sistema de gerenciamento de e-commerce desenvolvido em Python utilizando banco de dados Neo4j e arquitetura MVC (Model-View-Controller).

## Funcionalidades

- Gerenciamento de Usuarios (criar, editar, listar, pesquisar)
- Gerenciamento de Vendedores (criar, editar, listar, pesquisar)
- Gerenciamento de Produtos (criar, editar, listar, pesquisar)
- Gerenciamento de Compras (criar, listar, pesquisar)

## Arquitetura

O projeto segue o padrao MVC (Model-View-Controller):

- **Models**: Camada de acesso aos dados (Neo4j)
- **Views**: Camada de apresentacao (interface com usuario)
- **Controllers**: Camada de logica de negocio

## Requisitos

- Python 3.7+
- Neo4j 4.0+

## Instalacao

1. Clone o repositorio ou baixe os arquivos

2. Instale as dependencias:
```bash
pip install -r requirements.txt
```

3. Configure o Neo4j:
   - Instale o Neo4j (https://neo4j.com/download/)
   - Inicie o servidor Neo4j
   - Acesse http://localhost:7474
   - Configure usuario e senha

4. Edite o arquivo `config.py` com suas credenciais do Neo4j:
```python
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "sua_senha"
```

## Execucao

Execute o sistema com:
```bash
python main.py
```

## Estrutura do Projeto

```
BDNREX5/
├── models/
│   ├── usuario_model.py
│   ├── vendedor_model.py
│   ├── produto_model.py
│   └── compra_model.py
├── views/
│   ├── menu_view.py
│   ├── usuario_view.py
│   ├── vendedor_view.py
│   ├── produto_view.py
│   └── compra_view.py
├── controllers/
│   ├── usuario_controller.py
│   ├── vendedor_controller.py
│   ├── produto_controller.py
│   └── compra_controller.py
├── main.py
├── database.py
├── config.py
└── requirements.txt
```

## Uso

Ao executar o sistema, voce tera acesso a um menu interativo com as seguintes opcoes:

1. Gerenciar Usuarios
2. Gerenciar Vendedores
3. Gerenciar Produtos
4. Gerenciar Compras

Cada opcao possui submenus para criar, editar, listar e pesquisar registros.