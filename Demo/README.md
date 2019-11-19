# Demostração utilizando kafka-python
Podemos dizer que este demo está subdividido em três partes:
## Imagem para auxilio:
Podemos imaginar este demo de aplicação utilizando uma analogia a um restaurante.

![Restaurante](https://p70.f4.n0.cdn.getcloudapp.com/items/bLup9Gmj/Image+2019-11-18+at+9.18.05+PM.png?v=8dfd72e634760f8f381042dbbf5518e2)

## Exemplo de producer:

O código representado pelo arquivo `producer-raw-recipies.py` é análogo ao Fornecedor de matéria prima

Basicamente ao rodar o arquivo. Um Crawler acessara um site e pegará todos os dados deles publicando-os em um tópico chamado raw-recipes.

Imagine que isso possa ser um flow continuo de dados...

## Exemplo de consumers/producer
![molho](https://p70.f4.n0.cdn.getcloudapp.com/items/xQuv20bL/Image+2019-11-18+at+9.25.59+PM.png?v=7f9320cfc520a080518ef90f30060cea)

Como podemos visualizar pela analogia, o arquivo `producer_consumer_parse_recipes.py` se passa como um chefe que está pegando as matérias primas que é um tomate (raw-recipes) e á está refinando em um molho (parsed_recipes - dados mais tratados). 

Basicamente ao rodar o arquivo. O consumer vê o flow de dados fornecidos em `raw-recipes` trata os dados e publica em outro topico `parser_recipes` um conteudo que ficara de acesso para outros consumers(chefes).

## Exemplo de consumer - Outro chefe 
Imaginando que outro chefe possa consumir o molho deixado no armazem (tópico - parsed_recipes) e criar algo que tenha valor pro mesmo.

![Pizza](https://p70.f4.n0.cdn.getcloudapp.com/items/RBu0jXZg/Image+2019-11-18+at+9.34.08+PM.png?v=f639fae6610a6810127672a8197934fd
)

O arquivo `consumer-notification.py` representa neste caso, a parte final da aplicação. 

Basicamente ao rodar o código, ele irá pedir um input do usuário(sabor da pizza) e irá consumir os dados fornecidos pelo tópico `parsed_recipes` e dar uma resposta valida ao usuario conforme o seu input e os dados.

Caso rode todos ao mesmo tempo será possivel visualizar o funcionamento por um todo da aplicação.
![gif](https://p70.f4.n0.cdn.getcloudapp.com/items/p9uzJ5DQ/Screen+Recording+2019-11-18+at+09.48+PM.gif?v=ab0cb26e6f83e0535e0b3057b074670c)

Este gif foi feito rodando os três arquivos e lendo os dois tópicos para visualizar as mensagens sendo publicadas.

O código é de fácil compreensão e tem intuito demonstrativo, caso apareça qualquer duvida não hesite em perguntar.  

[@AntonioAndraues]( https://github.com/AntonioAndraues )







