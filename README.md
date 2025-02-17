# Inventário de Computadores
Caso tente abrir pelo celular, alguns navegadores podem forçar HTTPS automaticamente e impedir o acesso. Se isso acontecer, sugiro abrir no computador, onde o acesso funciona normalmente via HTTP.
## Descrição

Este sistema foi desenvolvido para gerenciar o inventário de computadores. Ele permite cadastrar, editar, listar e excluir registros de computadores.

### Funcionalidades

- Cadastro de computadores com informações como nome, fabricante, modelo, serial, data de aquisição, sistema operacional e setor.
- Edição de registros existentes.
- Exclusão de computadores cadastrados.
- Busca rápida por qualquer informação cadastrada.
- Interface simples e intuitiva para gerenciamento.

## Tecnologias Utilizadas

- Back-end: Flask (Python) para gerenciar as rotas e processar as solicitações.
- Banco de Dados: SQLite para armazenamento local dos registros.
- Front-end: HTML, CSS e JavaScript para a interface do usuário.
- Deploy: AWS Elastic Beanstalk para hospedar e disponibilizar a aplicação na nuvem.

## Acesso ao Sistema

[Acesse o sistema aqui](http://flask-env.eba-pimaq7yt.sa-east-1.elasticbeanstalk.com)

## Como Rodar Localmente

Caso queira executar localmente, siga os passos:

1. Clone o repositório:
   ```sh
   git clone https://github.com/Passetti-cmd/flask-api-inventario.git
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Execute o servidor Flask:
   ```sh
   python application.py
   ```
4. Acesse no navegador: `http://localhost:5000`

---
desenvolvido como parte de um desafio da empresa Bliss.
Erick Rene Vieira Passetti
