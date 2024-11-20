Para o problema de **gestão de banco de dados para um hotel**, podemos projetar um esquema de banco de dados que inclua quatro tabelas principais: `quartos`, `hospedes`, `reservas` e `funcionarios`. Abaixo está o plano completo para o banco de dados, incluindo o modelo de tabelas, inserção de dados fictícios e as consultas para realizar as operações de CRUD.

### 1. Esquema do Banco de Dados

#### Tabelas e Relacionamentos:

- **Tabela `quartos`:** Guarda informações sobre os quartos do hotel.
- **Tabela `hospedes`:** Guarda informações sobre os hóspedes.
- **Tabela `reservas`:** Relaciona hóspedes aos quartos, com as datas de check-in e check-out.
- **Tabela `funcionarios`:** Contém dados sobre os funcionários e suas tarefas.

### 2. Criação das Tabelas (DDL)

```sql
-- Tabela quartos
CREATE TABLE quartos (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    tipo ENUM('simples', 'duplo', 'suite') NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    status ENUM('disponivel', 'reservado', 'ocupado') DEFAULT 'disponivel' NOT NULL
);

-- Tabela hospedes
CREATE TABLE hospedes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    documento_identificacao VARCHAR(20) UNIQUE NOT NULL,
    contato VARCHAR(50) NOT NULL
);

-- Tabela funcionarios
CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    horario_trabalho TIME NOT NULL
);

-- Tabela reservas
CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_hospede INT,
    id_quarto INT,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    FOREIGN KEY (id_hospede) REFERENCES hospedes(id),
    FOREIGN KEY (id_quarto) REFERENCES quartos(id)
);
```

### 3. Inserção de Dados Fictícios

#### Inserindo Quartos

```sql
INSERT INTO quartos (tipo, preco, status) VALUES 
('simples', 100.00, 'disponivel'), 
('duplo', 150.00, 'disponivel'),
('suite', 200.00, 'disponivel'), 
('simples', 100.00, 'ocupado'),
('duplo', 150.00, 'reservado'),
('suite', 200.00, 'disponivel'),
('simples', 100.00, 'reservado'), 
('duplo', 150.00, 'ocupado'),
('suite', 200.00, 'disponivel'), 
('simples', 100.00, 'disponivel'), 
('duplo', 150.00, 'reservado'),
('suite', 200.00, 'disponivel'), 
('simples', 100.00, 'ocupado'), 
('duplo', 150.00, 'disponivel'),
('suite', 200.00, 'reservado');
```

#### Inserindo Hóspedes

```sql
INSERT INTO hospedes (nome, documento_identificacao, contato) VALUES
('Goku Silva', '12345678901', '1234-5678'),
('FreezaOliveira', '98765432101', '2345-6789'),
('Garlic Pereira', '12345987654', '3456-7890'),
('Raditz Costa', '11223344556', '4567-8901'),
('Gohan Lima', '22334455667', '5678-9012'),
('Trunks Souza', '33445566778', '6789-0123'),
('Yamcha Alves', '44556677889', '7890-1234'),
('Tenshin Lima', '55667788990', '8901-2345'),
('Caos Santos', '66778899001', '9012-3456'),
('Majin Martins', '77889900112', '0123-4567'),
('Cooler Costa', '88990011223', '1234-5678'),
('Nappa Gomes', '99001122334', '2345-6789'),
('Vegeta mendes', '10111223345', '3456-7890'),
('Broly Oliveira', '11223344567', '4567-8901'),
('Mestre Kame', '12334455678', '5678-9012');
```

#### Inserindo Funcionários

```sql
INSERT INTO funcionarios (nome, cargo, horario_trabalho) VALUES
('Ana Maria', 'Recepcionista', '08:00:00'),
('Carlos Roberto', 'Camareiro', '09:00:00'),
('Juliana Lima', 'Recepcionista', '07:30:00'),
('Lucas Souza', 'Gerente', '08:00:00'),
('Fernanda Santos', 'Camareira', '09:30:00'),
('Ricardo Oliveira', 'Segurança', '10:00:00'),
('Paula Costa', 'Gerente', '08:30:00'),
('Rafael Gomes', 'Camareiro', '07:00:00'),
('Eduardo Silva', 'Recepcionista', '08:15:00'),
('Roberta Souza', 'Segurança', '10:30:00'),
('Daniela Martins', 'Recepcionista', '07:45:00'),
('Juliano Santos', 'Camareiro', '09:00:00'),
('Mariana Oliveira', 'Camareira', '09:00:00'),
('Claudia Ferreira', 'Recepcionista', '08:00:00'),
('Simone Costa', 'Gerente', '08:30:00');
```

#### Inserindo Reservas

```sql
INSERT INTO `reservas`(`id`, `id_hospede`, `id_quarto`, `data_checkin`, `data_checkout`) 
VALUES ('[value-1]','4','5','2024-11-19','2024-11-26'),
('[value-1]','6','7','2024-11-19','2024-11-27'),
('[value-1]','8','9','2024-11-19','2024-11-28'),
('[value-1]','11','12','2024-11-19','2024-11-29'),
('[value-1]','13','1','2024-11-19','2024-11-30'),
('[value-1]','14','15','2024-11-19','2024-11-01'),
('[value-1]','16','17','2024-11-19','2024-11-02'),
('[value-1]','18','19','2024-11-19','2024-11-03'),
('[value-1]','20','21','2024-11-19','2024-12-04'),
('[value-1]','22','23','2024-11-19','2024-12-05'),
('[value-1]','24','25','2024-11-19','2024-12-06'),
('[value-1]','26','30','2024-11-19','2024-12-07)


```

### 4. Consultas para Operações CRUD

#### **Create:**

Já realizamos a inserção de dados fictícios para hóspedes, quartos, funcionários e reservas. 

#### **Read:**

1. **Listar todos os quartos disponíveis, incluindo informações sobre tipo e status:**

```sql
SELECT tipo, preco, status 
FROM quartos 
WHERE status = 'disponivel';
```

2. **Listar todos os hóspedes que têm reservas para um período específico (por exemplo, entre 2024-11-01 e 2024-11-10):**

```sql
SELECT h.nome, r.data_checkin, r.data_checkout
FROM hospedes h
JOIN reservas r ON h.id = r.id_hospede
WHERE r.data_checkin BETWEEN '2024-11-01' AND '2024-11-10';
```

3. **Listar todos os quartos reservados por um hóspede específico (por exemplo, hóspede com ID = 1):**

```sql
SELECT q.tipo, q.preco, r.data_checkin, r.data_checkout
FROM quartos q
JOIN reservas r ON q.id = r.id_quarto
WHERE r.id_hospede = 1;
```

#### **Update:**

1. **Atualizar o nome de um hóspede (por exemplo, o hóspede com ID = 1):**

```sql
UPDATE hospedes 
SET nome = 'Goku Pedro Silva' 
WHERE id = 1;
```

2. **Alterar o status de um quarto de "disponível" para "ocupado" após uma reserva:**

```sql
UPDATE quartos 
SET status = 'ocupado' 
WHERE id = 2;
```

#### **Delete:**

1. **Excluir uma reserva específica e garantir que os dados de hóspedes e quartos não sejam afetados (por exemplo, reserva com ID = 5):**

```sql
DELETE FROM reservas 
WHERE id = 5;
```

