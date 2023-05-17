# CEAD Solicitações

O CEAD Solicitações é um sistema interno do CEAD para otimização das solicitações de demandas de alunos e coordenadores dos cursos oferecidos pelo CEAD.

---

## Inicialização

1. Clonar esse repositório e acessar a raiz do código rodando `cd CEADSolicitacoes/`
2. Criar seu ambiente virtual:
    - Windows:
    ```bash
    python -m venv env
    ```

    - Linux:
    ```bash
    virtualenv env
    ```

3. Inicializar o ambiente virtual rodando:
    
    - Windows:
    ```powershell
    . .\env\Scripts\activate
    ```

    - Linux:
    ```bash
    . ./env/bin/activate
    ```

4. Instalação dos requisitos da aplicação, rodando `pip install -r requirements.txt`
5. Criar na raiz do projeto o arquivo **.env** contendo os dados sensíveis da aplicação conforme o exemplo a seguir:

    ```env
    SECRET_KEY=your-secure-secret-key
    DEBUG=<True | False>
    ```

6. Fazer a migração da aplicação para o banco de dados rodando `python manage.py migrate`