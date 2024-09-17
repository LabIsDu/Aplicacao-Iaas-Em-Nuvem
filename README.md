
# Aplicação na Nuvem Iaas


Realização da implantação de uma aplicação em uma máquina virtual na nuvem, utilizando infraestrutura como serviço (IaaS). A máquina virtual foi controlada remotamente por meio de SSH, permitindo a configuração e gerenciamento do ambiente. A aplicação foi containerizada com Docker e gerenciada via Docker Compose, garantindo escalabilidade, isolamento e facilidade de manutenção em ambiente de produção.
A aplicação possui duas rotas que gerem acesso a informações de um banco de dados gerado com MySql, a primeira rota consulta informações da tabela, como nome e colunas existentes enquanto a segunda rota, nomeada como 'data',exibe o banco completo.


## Instalação

```bash
 Configure o acesso com ssh para controlar remotamente a VM

@example

  > ssh -i .\certificado.pem ubuntu@IpDaMaquina

  crie uma pasta para a aplicação e configure tudo dentro dela

  > mkdir meu-app
  cd meu-app

 Copie e cole o codigo de cada arquivo:

  >meu-app> nano Dockerfile
  >meu-app> nano requirements.txt
  >meu-app> nano database.py
  >meu-app> nano app.py
  
  obs: execute o script database.py e certifique-se de que o banco foi criado antes de prosseguir.

 Builde e execute o docker compose:

  >meu-app> sudo docker build -t app:latest .
  >meu-app> sudo docker run -t -p 80:80 app:latest


```

## Demonstração:

    
## Referência

 - [Building a Flask Application with MySQL Database Using Docker Compose](https://www.linkedin.com/pulse/building-flask-application-mysql-database-using-docker-agarwal/)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)



