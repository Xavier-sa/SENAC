## Enunciado de Banco de Dados para Gestão de Hotel
## Você foi contratado para desenvolver o banco de dados para um hotel que deseja
## gerenciar os dados de quartos, hóspedes, reservas e funcionários. A atividade consiste
## em projetar o esquema do banco de dados e realizar operações básicas de 
## CRUD
## (Create, Read, Update, Delete).


## 1. Descrição do Problema
## O hotel precisa armazenar informações sobre:
## • Quartos disponíveis no hotel, incluindo detalhes como tipo (simples, duplo,
## suíte), preço e status (disponível, reservado, ocupado).
## • Hóspedes que se hospedam no hotel, incluindo informações como nome,
## documento de identificação e contato.
## • Reservas, que associam hóspedes aos quartos, incluindo datas de check-in e
## check-out.
## • Funcionários, que trabalham no hotel, com informações sobre nome, cargo e
## horário de trabalho.
### Cada quarto pode ser associado a várias reservas (relacionamento de um para muitos), e
## cada reserva deve estar associada a um hóspede. Além disso, cada funcionário é
## responsável por uma determinada tarefa no hotel.
## Garanta que cada tabela tenha uma chave primária para identificação única e defina
## chaves estrangeiras para os relacionamentos entre as tabelas (quartos, reservas,
## hóspedes e funcionários).

----------

## 2. Requisitos de Implementação
## a) Crie o esquema do banco de dados com pelo menos quatro tabelas relacionadas:
## quartos, hóspedes, reservas e funcionários. EXECUTADO
## b) Insira registros fictícios suficientes para ilustrar a relação entre as tabelas.
## c) Realize consultas e operações de manipulação de dados com base nos seguintes
## cenários:

-------
## 3. Operações CRUD
## Create:
## • Cadastre pelo menos 25 hóspedes, 25 quartos e 35 funcionários.
## • Realize pelo menos 15 reservas para associar hóspedes aos quartos.
## • Certifique-se de que cada reserva esteja associada a um hóspede e a um quarto,
## com as datas de check-in e check-out.
## Read:
## • a) Liste todos os quartos disponíveis, incluindo informações sobre o tipo e o
## status de cada um.
## • b) Liste todos os hóspedes que têm reservas para um período específico.
## • c) Liste todos os quartos reservados por um hóspede específico.
Update:
• Atualize o nome de um hóspede e reflita essa alteração nas consultas.
• Modifique o status de um quarto de "disponível" para "ocupado" após uma
reserva ser realizada.
Delete:
• Exclua uma reserva específica e verifique se a exclusão não afetou os registros
de outros hóspedes, quartos ou funcionários.
4. Entrega
Apresente os scripts SQL que implementem as tabelas com suas chaves primárias e
estrangeiras, as inserções de dados e as consultas realizadas.