Objetivo
========

O objetivo do projeto é criar uma estrutura de ETL simples, que faça a leitura dos arquivos .txt e usando os dados enriqueça-os com a api de geolocalização reversa do googlemaps e então disponha eles usando um dataframe .

Requisitos
==========

Os seguintes componentes são requisitos para o funcionamento correto do programa:
* Python 3.5.x ou mais recente;
* Mysql workbench instalado e com ao menos uma instância;
* mysql.connector instalado (instalação via pip)
* glob instalado (instalação via pip)
* pandas instalado (instalação via pip)

Passo a passo:
=============
* **1 - Clone este repositório para sua máquina**

* **2 -  No arquivo main.py coloque a senha e o usuário da instância do mysql**
```
import crud
import geoapi
import glob
import pandas as pd
import ddl

#criação das estruturas de dados INSIRA SENHA E USUÁRIO AQUI
db = ddl.createStructure("colocar usuario aqui","colocar senha aqui","localhost")


```
* **3 - Via prompt acesse o caminho até a sua pasta então rode o comando "python3 main.py"**

* **4 O programa vai alimentar a base de dados com a informação enriquecida e então vai dar o display no formato de um dataframe(o programa exibe um log de cada requisição concluída)**

Melhorias futuras:
=================
Certamente o programa como está hoje é algo muito simples que serve apenas para mostrar meu conhecimento com ETL,requisições de api e de programação no geral. Desde o começo meu plano era criar uma interface com django para mostrar as informações e ainda alguns gráficos com métricas analisadas. Eu também colocaria o banco de dados para a nuvem e faria diversos testes de otimização. Eu tive pouco tempo pra me dedicar a esse projeto essa semana e fico muito feliz com o resultado que obtive, no entanto tem muito que ser otimizado para ter um produto de alta qualidade.

Métricas propostas:
==================
Podemos analisar diversas métricas nos dados.Partindo do presuposto que são dados de clientes e/ou usuários algumas são:
* Clientes/usuários por bairro;
* Clientes/usuários por cidade;
* Cidades com mais clientes/usuários;
* Zonas territorias com maior número de clientes/usuários.

Usando dessas informações poderiamos analisar em qual área seria mais interessante fazer uma campanha de marketing ou uma ação de vendas. Ainda poderiamos usar os dados para cruzar com outras informações afim de descobrir a expctativa de gasto das pessoas que moram/frequentam aquela localização.Poderiamos também analisar que tipo de produto seria mais interessante vender em uma área com o volume maior de pessoas e que tipo vender em uma área com volume menor.Além disso tudo ao ter essas informações em mãos podemos usar elas combinadas com outras apis e serviços para obter mais informações e enriquecer ainda mais a inteligência do negócio
