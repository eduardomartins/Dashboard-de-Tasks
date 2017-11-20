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
[![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/eduardomartins/Dashboard-de-Tasks/master/docs/img/arquivos3.png)]

### Authors

* **Eduardo Sant'Anna Martins** - *Initial work* - [eduardimartins](https://github.com/eduardomartins)


