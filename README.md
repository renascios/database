# Projeto Python e Banco de Dados

Projeto de aprendizado para praticar Python e SQLite. A aplicação oferece um menu de terminal para cadastrar, listar, buscar, atualizar e excluir produtos. O projeto não está completo, alterações devem ser feitas no futuro.

## Arquivos do projeto

- `main.py` — ponto de entrada da aplicação. Exibe o menu, recebe os dados pelo terminal e chama as funções de `database.py`.
- `database.py` — implementa o acesso ao SQLite e as operações CRUD para a tabela `produtos`.
- `database.db` — banco SQLite usado pela aplicação. A tabela é criada quando o programa inicia; os dados ficam salvos entre execuções.
- `teste.py` — script experimental que se conecta a `exemplo.db`. Contém exemplos de comandos SQL comentados e uma conversão inválida (`int("string")`), que gera um erro ao ser executada.
- `exemplo.db` — banco SQLite usado pelo script experimental `teste.py`.
- `.venv/` — ambiente virtual Python local, se presente. Não é necessário para executar o projeto.
- `__pycache__/` — arquivos temporários gerados pelo Python.

## Requisitos

- Python 3
- SQLite, utilizado pelo módulo `sqlite3` incluído na biblioteca padrão do Python

Não há dependências externas.

## Como executar

No terminal, a partir da pasta do projeto:

```bash
python main.py
```

O programa cria a tabela `produtos` em `database.db` caso ela ainda não exista. Use as opções do menu para manipular os produtos e escolha `6` para sair.

## Operações implementadas

- Criar a tabela de produtos.
- Cadastrar um produto com nome, quantidade e preço.
- Listar todos os produtos.
- Buscar um produto pelo ID.
- Atualizar os dados de um produto.
- Excluir um produto pelo ID.
- Validar os dados recebidos pelas funções de acesso ao banco.
