-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 20/11/2024 às 02:44
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `provabd_hotelwx`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionarios`
--

CREATE TABLE `funcionarios` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `cargo` varchar(100) NOT NULL,
  `horario_trabalho` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `funcionarios`
--

INSERT INTO `funcionarios` (`id`, `nome`, `cargo`, `horario_trabalho`) VALUES
(1, 'Ana Maria', 'Recepcionista', '08:00:00'),
(2, 'Carlos Roberto', 'Camareiro', '09:00:00'),
(3, 'Juliana Lima', 'Recepcionista', '07:30:00'),
(4, 'Lucas Souza', 'Gerente', '08:00:00'),
(5, 'Fernanda Santos', 'Camareira', '09:30:00'),
(6, 'Ricardo Oliveira', 'Segurança', '10:00:00'),
(7, 'Paula Costa', 'Gerente', '08:30:00'),
(8, 'Rafael Gomes', 'Camareiro', '07:00:00'),
(9, 'Eduardo Silva', 'Recepcionista', '08:15:00'),
(10, 'Roberta Souza', 'Segurança', '10:30:00'),
(11, 'Daniela Martins', 'Recepcionista', '07:45:00'),
(12, 'Juliano Santos', 'Camareiro', '09:00:00'),
(13, 'Mariana Oliveira', 'Camareira', '09:00:00'),
(14, 'Claudia Ferreira', 'Recepcionista', '08:00:00'),
(15, 'Simone Costa', 'Gerente', '08:30:00');

-- --------------------------------------------------------

--
-- Estrutura para tabela `hospedes`
--

CREATE TABLE `hospedes` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `documento_identificacao` varchar(20) NOT NULL,
  `contato` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `hospedes`
--

INSERT INTO `hospedes` (`id`, `nome`, `documento_identificacao`, `contato`) VALUES
(1, 'Goku Pedro Silva', '12345678901', '1234-5678'),
(2, 'FreezaOliveira', '98765432101', '2345-6789'),
(3, 'Garlic Pereira', '12345987654', '3456-7890'),
(4, 'Raditz Costa', '11223344556', '4567-8901'),
(5, 'Gohan Lima', '22334455667', '5678-9012'),
(6, 'Trunks Souza', '33445566778', '6789-0123'),
(7, 'Yamcha Alves', '44556677889', '7890-1234'),
(8, 'Tenshin Lima', '55667788990', '8901-2345'),
(9, 'Caos Santos', '66778899001', '9012-3456'),
(10, 'Majin Martins', '77889900112', '0123-4567'),
(11, 'Cooler Costa', '88990011223', '1234-5678'),
(12, 'Nappa Gomes', '99001122334', '2345-6789'),
(13, 'Vegeta mendes', '10111223345', '3456-7890'),
(14, 'Broly Oliveira', '11223344567', '4567-8901'),
(15, 'Mestre Kame', '12334455678', '5678-9012');

-- --------------------------------------------------------

--
-- Estrutura para tabela `quartos`
--

CREATE TABLE `quartos` (
  `id` int(11) NOT NULL,
  `tipo` enum('simples','duplo','suite') NOT NULL,
  `preco` decimal(10,2) NOT NULL,
  `status` enum('disponivel','reservado','ocupado') NOT NULL DEFAULT 'disponivel'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `quartos`
--

INSERT INTO `quartos` (`id`, `tipo`, `preco`, `status`) VALUES
(1, 'simples', 100.00, 'disponivel'),
(2, 'duplo', 150.00, 'disponivel'),
(3, 'suite', 200.00, 'disponivel'),
(4, 'simples', 100.00, 'ocupado'),
(5, 'duplo', 150.00, 'reservado'),
(6, 'suite', 200.00, 'disponivel'),
(7, 'simples', 100.00, 'reservado'),
(8, 'duplo', 150.00, 'ocupado'),
(9, 'suite', 200.00, 'disponivel'),
(10, 'simples', 100.00, 'disponivel'),
(11, 'duplo', 150.00, 'reservado'),
(12, 'suite', 200.00, 'disponivel'),
(13, 'simples', 100.00, 'ocupado'),
(14, 'duplo', 150.00, 'disponivel'),
(15, 'suite', 200.00, 'reservado');

-- --------------------------------------------------------

--
-- Estrutura para tabela `reservas`
--

CREATE TABLE `reservas` (
  `id` int(11) NOT NULL,
  `id_hospede` int(11) DEFAULT NULL,
  `id_quarto` int(11) DEFAULT NULL,
  `data_checkin` date NOT NULL,
  `data_checkout` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `reservas`
--

INSERT INTO `reservas` (`id`, `id_hospede`, `id_quarto`, `data_checkin`, `data_checkout`) VALUES
(46, 2, 3, '2024-11-19', '2024-11-25'),
(59, 6, 7, '2024-11-19', '2024-11-27'),
(60, 8, 9, '2024-11-19', '2024-11-28');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `funcionarios`
--
ALTER TABLE `funcionarios`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `hospedes`
--
ALTER TABLE `hospedes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `documento_identificacao` (`documento_identificacao`);

--
-- Índices de tabela `quartos`
--
ALTER TABLE `quartos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_hospede` (`id_hospede`),
  ADD KEY `id_quarto` (`id_quarto`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `funcionarios`
--
ALTER TABLE `funcionarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `hospedes`
--
ALTER TABLE `hospedes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `quartos`
--
ALTER TABLE `quartos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `reservas`
--
ALTER TABLE `reservas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`id_hospede`) REFERENCES `hospedes` (`id`),
  ADD CONSTRAINT `reservas_ibfk_2` FOREIGN KEY (`id_quarto`) REFERENCES `quartos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
