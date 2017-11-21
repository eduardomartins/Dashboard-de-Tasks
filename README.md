# Dashboard de Taks

### Prerequisitos

Ter instalado o virtualenv 

```
$ [sudo] pip install virtualenv
```

[link de instalção do virtual env](https://virtualenv.pypa.io/en/stable/installation/)

### Instalação

Iniciar o virtual env

```
$ [sudo] virtualenv env
```

Para iniciar o ambiente

```
$ source env/bin/activate
```

Instalar as bibliotecas requeridas, que se encontram no aquivo requirements.txt

```
$ pip install -r requirements.txt
```


### Para executar

**OBSERVAÇÃO: No diretório "Dashboard-de-Tasks/tasks/tasks/" tem um arquivo secrets.py.zip com algumas informações "sensíveis", porém necessárias para a aplicação. Para executá-la, e só descompactar o arquivo no próprio local, usando a senha**

Entre na pasta tasks

tasks/

├── manage.py


Executar esse comanda para craiar uma banco de dados local (sqlite3)
```
$ python manage.py migrate
```

Executar esse comando para iniciar o servidor web de testes

```
$ python manage.py runserver
```

**NOTA: a porta 8000 e localhost devem estar disponíveis**

Agora é só abrir o browser no endereço: 

[http://localhost:8000](http://localhost:8000)

## Modo de uso

Primeiro digite o endereço no browser [http://localhost:8000](http://localhost:8000).

Clique no no boto para acessar o Dashboard
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/home.png)

Clique para fazer o login no Google+
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/login.png)

Você será redirecionado para o Dashboard
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/dashboard.png)

Crie uma nova tarefa clicando no botão "Nova tarefa" e preencha 
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/nova-tarefa.png)

Selecione os arquivos
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/arquivos3.png)

Nova terefa salva
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/nova-salva.png)

Click em "Editar" a tarefa
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/editar.png)

Edição salva
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/edicao-salva.png)

Clique no botão excluir para excluir uma tarefa
![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/excluir.png)


### Authors

* **Eduardo Sant'Anna Martins** - *Initial work* - [eduardimartins](https://github.com/eduardomartins)


