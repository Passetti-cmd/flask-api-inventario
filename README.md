# Inventário de Computadores

## Descrição
Este sistema foi desenvolvido para gerenciar o inventário de computadores de uma organização. Ele permite cadastrar, editar, listar e excluir registros de computadores, facilitando o controle e a gestão dos equipamentos.

### Funcionalidades
- Cadastro de computadores com informações como nome, fabricante, modelo, serial, data de aquisição, sistema operacional e setor.
- Edição de registros existentes.
- Exclusão de computadores cadastrados.
- Busca rápida por qualquer informação cadastrada.
- Interface simples e intuitiva para gerenciamento.

## Tecnologias Utilizadas
- **Back-end:** Flask (Python) para gerenciar as rotas e processar as solicitações.
- **Banco de Dados:** SQLite para armazenamento local dos registros.
- **Front-end:** HTML, CSS e JavaScript para a interface do usuário.
- **Deploy:** AWS Elastic Beanstalk para hospedar e disponibilizar a aplicação na nuvem.

## Acesso ao Sistema
[Acesse o sistema aqui](http://flask-env.eba-pimaq7yt.sa-east-1.elasticbeanstalk.com) *(substituir pelo link real do deploy na AWS)*

## Como Rodar Localmente
Caso queira executar localmente, siga os passos:
1. Clone o repositório:  
   ```sh
   git clone https://github.com/SeuUsuario/flask-api-inventario.git
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

Projeto desenvolvido como parte de um desafio técnico.

