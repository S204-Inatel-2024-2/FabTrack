# Sobre o FabTrack

FabTrack é um aplicativo projetado para simplificar o processo de fila de impressão 3D. Ele simplifica o processo de orçamento tanto para clientes quanto para prestadores de serviços, tornando mais fácil gerenciar projetos de impressão 3D.

## Recursos

- Gerenciamento eficiente de fila: o FabTrack permite que os usuários acompanhem e priorizem facilmente os trabalhos de impressão 3D, garantindo um fluxo de trabalho tranquilo.
- Orçamento sem complicações: com o FabTrack, os clientes podem solicitar rapidamente orçamentos para seus projetos, enquanto os prestadores de serviços podem gerar orçamentos precisos e competitivos sem esforço.
- Atualizações em tempo real: fique informado sobre o status de seus trabalhos de impressão 3D com as atualizações em tempo real do FabTrack, garantindo transparência e comunicação eficaz.

## Como rodar o projeto

Para rodar o projeto, siga as etapas abaixo:

1. Clone o repositório do projeto do GitHub para o seu diretório local:

    ```bash
    git clone https://github.com/S204-Inatel-2024-2/FabTrack
    ```

2. Crie um ambiente virtual para isolar as dependências do projeto:

    ```bash
    python -m venv env
    ```

3. Ative o ambiente virtual:

    - No Windows:

      ```bash
      env\Scripts\activate
      ```

    - No macOS e Linux:

      ```bash
      source env/bin/activate
      ```

4. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

7. Para iniciar o banco de dados, execute o comando abaixo para rodar o Docker Compose:

    ```bash
    docker-compose up -d
    ```

8. Abra o navegador e acesse `http://localhost:8000` para ver o projeto em execução.

