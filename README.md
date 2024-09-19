
# Aplicação na Nuvem Iaas

Realizamos a implantação de uma aplicação em uma máquina virtual na nuvem, utilizando infraestrutura como serviço (IaaS). A máquina virtual foi controlada remotamente via SSH, permitindo configurar e gerenciar o ambiente. A aplicação foi containerizada com Docker e gerenciada através de Docker Compose, garantindo escalabilidade, isolamento e facilidade de manutenção em ambiente de produção.

A aplicação possui três rotas principais. A rota padrão (/) faz uma consulta ao banco de dados SQLite e exibe os nomes das tabelas existentes. A segunda rota (/data) retorna o conteúdo completo do banco de dados, enquanto a terceira rota (/external) utiliza um serviço separado por meio da biblioteca requests, que faz uma chamada a uma API externa e exibe dados fictícios retornados pela mesma.

## Equipe Responsável pela execução do Projeto

- Adão Eduardo Gomes de Oliveira | Matricula: 2023010692
- Alexandra Silva de Paula | Matrícula: 2023018832
- Carlos Eduardo de Lima Lira Santana | Matrícula: 2023010629
- Gustavo Ferreira Reinaldo | Matricula: 2023010997
- Sayonara Arcanjo da Silva | Matrícula: 2023011107

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
  >meu-app> nano docker-compose.yml
  >meu-app> nano requirements.txt
  >meu-app> nano db_init.py
  >meu-app> nano app.py
  >meu-app> nano requests_worker.py
  
  obs: execute o script db_init.py e certifique-se de que o banco foi criado antes de prosseguir.

 Builde e execute o docker compose:

 >meu-app> sudo docker compose up

 lembre-se de usar o ip da maquina virtual.


```

## Demonstração:

    
## Referência

 - [Building a Flask Application with MySQL Database Using Docker Compose](https://www.linkedin.com/pulse/building-flask-application-mysql-database-using-docker-agarwal/)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)



