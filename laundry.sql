-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Окт 14 2018 г., 06:53
-- Версия сервера: 8.0.12
-- Версия PHP: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `laundry`
--

-- --------------------------------------------------------

--
-- Структура таблицы `customer`
--

CREATE TABLE `customer` (
  `ID_Customer` int(11) NOT NULL,
  `First_Name_Customer` char(18) DEFAULT NULL,
  `Second_Name_Customer` char(18) DEFAULT NULL,
  `Phone_Customer` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'Не указан'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `customer`
--

INSERT INTO `customer` (`ID_Customer`, `First_Name_Customer`, `Second_Name_Customer`, `Phone_Customer`) VALUES
(1, 'Juan', 'Rodriguez', '+34917853211'),
(2, 'Ana', 'Mena', '+34918897997'),
(3, 'Becky', 'G', '+34917892234'),
(4, 'Rodrigo', 'De Toledo', '+349250931233'),
(6, 'Pedro', 'Fernandez', '+34917853567'),
(7, 'Pedro', 'Rodriguez', '+34917859877'),
(9, 'Isabel', 'Perez', '+34916578945'),
(15, 'Emilia', 'Andrada', '+543517850355');

-- --------------------------------------------------------

--
-- Структура таблицы `employee`
--

CREATE TABLE `employee` (
  `ID_Employee` int(11) NOT NULL,
  `First_Name` char(18) DEFAULT NULL,
  `Second_Name` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Password` char(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Gender` tinyint(1) DEFAULT NULL,
  `Adress_Employee` char(18) DEFAULT NULL,
  `Mail` char(18) DEFAULT NULL,
  `Salary` int(11) DEFAULT NULL,
  `Position` char(18) DEFAULT NULL,
  `ID_Laundry` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `employee`
--

INSERT INTO `employee` (`ID_Employee`, `First_Name`, `Second_Name`, `Password`, `Gender`, `Adress_Employee`, `Mail`, `Salary`, `Position`, `ID_Laundry`) VALUES
(1, 'Semyon', 'Malykh', '0b9c5120ea86155f02d81e6f2f90c900', 1, NULL, NULL, NULL, NULL, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `employee_to_order`
--

CREATE TABLE `employee_to_order` (
  `ID_Order` int(11) NOT NULL,
  `ID_Employee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `employee_to_order`
--

INSERT INTO `employee_to_order` (`ID_Order`, `ID_Employee`) VALUES
(1, 1),
(73, 1),
(124, 1),
(139, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `item`
--

CREATE TABLE `item` (
  `ID_Item` int(11) NOT NULL,
  `Name` char(18) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `item`
--

INSERT INTO `item` (`ID_Item`, `Name`) VALUES
(1, 'T-Shirt');

-- --------------------------------------------------------

--
-- Структура таблицы `items_in_orders`
--

CREATE TABLE `items_in_orders` (
  `ID_Item` int(11) NOT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `ID_Order` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `items_in_orders`
--

INSERT INTO `items_in_orders` (`ID_Item`, `Quantity`, `ID_Order`) VALUES
(1, 2, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `laundry`
--

CREATE TABLE `laundry` (
  `ID_Laundry` int(11) NOT NULL,
  `Adress_Laundry` char(18) DEFAULT NULL,
  `Phone_Landry` char(18) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `laundry`
--

INSERT INTO `laundry` (`ID_Laundry`, `Adress_Laundry`, `Phone_Landry`) VALUES
(1, 'Madrid', '+34915557575');

-- --------------------------------------------------------

--
-- Структура таблицы `lorder`
--

CREATE TABLE `lorder` (
  `ID_Order` int(11) NOT NULL,
  `Date_Order` date DEFAULT NULL,
  `Date_Rendition` date DEFAULT NULL,
  `Status` tinyint(1) DEFAULT '0',
  `Cost` int(11) DEFAULT NULL,
  `Is_Payed` tinyint(1) DEFAULT NULL,
  `Date_Pay` date DEFAULT NULL,
  `ID_Customer` int(11) DEFAULT NULL,
  `ID_Laundry` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `lorder`
--

INSERT INTO `lorder` (`ID_Order`, `Date_Order`, `Date_Rendition`, `Status`, `Cost`, `Is_Payed`, `Date_Pay`, `ID_Customer`, `ID_Laundry`) VALUES
(1, '2018-10-12', '2018-10-12', 1, 123, 1, '2018-10-12', 1, 1),
(2, '2018-10-17', NULL, 0, 233, 1, '2018-10-17', 1, 1),
(73, '2018-12-31', NULL, 0, 2312, 1, NULL, 1, 1),
(78, '2018-12-31', NULL, 0, 123, 0, NULL, 1, 1),
(106, '2018-12-31', NULL, 0, 432, 1, NULL, 2, 1),
(115, '2018-12-31', NULL, 0, 342, 1, NULL, 3, 1),
(116, '2018-12-31', NULL, 0, 3423, 1, NULL, 4, 1),
(117, '2018-12-31', NULL, 0, 53, 1, NULL, 3, 1),
(119, '2018-12-31', NULL, 0, 3423, 1, NULL, 1, 1),
(121, '2018-10-10', '2018-10-12', 1, 432, 1, '2018-10-12', 7, 1),
(123, '2018-12-31', NULL, 0, 4231, 1, NULL, 1, 1),
(124, '2018-12-31', NULL, 0, 34, 0, NULL, 1, 1),
(125, '2018-12-31', NULL, 0, 432, 0, NULL, 1, 1),
(126, '2018-12-31', '2019-01-01', 1, 789, 1, '2018-12-31', 1, 1),
(127, '2018-10-12', NULL, 1, 654, 1, '2018-10-12', 7, 1),
(128, '2018-12-31', '2018-12-31', 1, 4321, 1, '2018-12-31', 7, 1),
(129, '2018-10-13', NULL, 0, 214, 1, NULL, 1, 1),
(131, '2018-10-13', NULL, 0, 312, 1, NULL, 9, 1),
(136, '2018-10-13', NULL, 0, 432, 1, NULL, 15, 1),
(137, '2018-10-13', NULL, 0, 532, 0, NULL, 15, 1),
(138, '2018-10-13', NULL, 0, 231, 1, NULL, 15, 1),
(139, '2018-10-13', NULL, 1, 32, 1, NULL, 9, 1);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ID_Customer`);

--
-- Индексы таблицы `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`ID_Employee`),
  ADD KEY `R_8` (`ID_Laundry`);

--
-- Индексы таблицы `employee_to_order`
--
ALTER TABLE `employee_to_order`
  ADD PRIMARY KEY (`ID_Order`,`ID_Employee`),
  ADD KEY `R_3` (`ID_Employee`);

--
-- Индексы таблицы `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`ID_Item`);

--
-- Индексы таблицы `items_in_orders`
--
ALTER TABLE `items_in_orders`
  ADD PRIMARY KEY (`ID_Item`,`ID_Order`),
  ADD KEY `R_6` (`ID_Order`);

--
-- Индексы таблицы `laundry`
--
ALTER TABLE `laundry`
  ADD PRIMARY KEY (`ID_Laundry`);

--
-- Индексы таблицы `lorder`
--
ALTER TABLE `lorder`
  ADD PRIMARY KEY (`ID_Order`),
  ADD KEY `R_4` (`ID_Customer`),
  ADD KEY `R_7` (`ID_Laundry`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `customer`
--
ALTER TABLE `customer`
  MODIFY `ID_Customer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT для таблицы `employee`
--
ALTER TABLE `employee`
  MODIFY `ID_Employee` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `item`
--
ALTER TABLE `item`
  MODIFY `ID_Item` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `laundry`
--
ALTER TABLE `laundry`
  MODIFY `ID_Laundry` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `lorder`
--
ALTER TABLE `lorder`
  MODIFY `ID_Order` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=140;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `R_8` FOREIGN KEY (`ID_Laundry`) REFERENCES `laundry` (`id_laundry`);

--
-- Ограничения внешнего ключа таблицы `employee_to_order`
--
ALTER TABLE `employee_to_order`
  ADD CONSTRAINT `R_1` FOREIGN KEY (`ID_Order`) REFERENCES `lorder` (`id_order`),
  ADD CONSTRAINT `R_2` FOREIGN KEY (`ID_Employee`) REFERENCES `employee` (`id_employee`),
  ADD CONSTRAINT `R_3` FOREIGN KEY (`ID_Employee`) REFERENCES `employee` (`id_employee`);

--
-- Ограничения внешнего ключа таблицы `items_in_orders`
--
ALTER TABLE `items_in_orders`
  ADD CONSTRAINT `R_5` FOREIGN KEY (`ID_Item`) REFERENCES `item` (`id_item`),
  ADD CONSTRAINT `R_6` FOREIGN KEY (`ID_Order`) REFERENCES `lorder` (`id_order`);

--
-- Ограничения внешнего ключа таблицы `lorder`
--
ALTER TABLE `lorder`
  ADD CONSTRAINT `R_4` FOREIGN KEY (`ID_Customer`) REFERENCES `customer` (`id_customer`),
  ADD CONSTRAINT `R_7` FOREIGN KEY (`ID_Laundry`) REFERENCES `laundry` (`id_laundry`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
