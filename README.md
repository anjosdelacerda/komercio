# Komercio Generic Views


**Resumo:**

A aplicação consiste no cadastro de usuários no banco e estes usuários poderão anunciar produtos para venda dentro da plataforma, tendo um relacionamento de 1:n entre o usuário e os produtos criados. A aplicação utiliza o PostgreSQL como banco relacional.

**Tecnologias utilizadas:**

Python | Django | Django Rest Framework | PostgreSQL | Serializers | Token | DOTENV | Generic Views

Para clonar o arquivo em sua máquina use o seguinte comando no seu terminal:

````
git clone git@github.com:anjosdelacerda/komercio.git
````

Para que a aplicação funcione será necessário instalar o Python em sua máquina, você encontrará informações de como fazer isso na <a href="https://docs.python.org/3/tutorial/">documentação</a>. 

O pip também será necessário para o gerenciamento de instalações de dependências, na <a href="https://pip.pypa.io/en/stable/getting-started/"> documentação </a> você terá um passo-a-passo de como instala-lo. 

**Atenção:** É necessário criar uma arquivo chamado .env dentro da pasta do projeto e colocar as suas credenciais nela, use o arquivo .env.example como
parâmetro. Para isso você terá que ter o **PostgreSQL** instalado em sua máquina, caso tenha dúvidas você poderá consultar a documentação <a href="https://www.postgresql.org/docs/current/tutorial-start.html">aqui</a>.

No terminal dentro da sua pasta clonada crie uma variável de abiente com este comando:

````
python -m venv venv
````

Agora ative este variável para que você possa instalas as dependências da aplicação com segurança:

````
source venv/bin/activate
````

Agora instale todas as dependências rodando este comando no terminal da pasta clonada:

````
pip install -r requirements.txt
````

Para ativar a aplicação para testagem das rotas:

````
python manage.py runserver
````

Dentro da aplicação haverá um arquivo chamado **workspace.json** aonde vocẽ poderá importa-lo em seu testador de rotas favorito.

Os dados armanezados poderão ser vistos dentro do database criado no PostgreSQL, os dados foram enviados pelo arquivo .env que deverá ser criado. Um nome recomendado para o database é komercio, mas fique a vontade para usar o que quiser. Ver os dados na database pelo terminal pode ser um pouco desagradável e confuso, porém você poderá usar o <a href="https://www.beekeeperstudio.io/get"> beekeeper </a> para visualizar as tabelas de forma estilizada.
