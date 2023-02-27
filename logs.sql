-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2023 at 11:35 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `portscanner`
--

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `id` int(11) NOT NULL,
  `date_time` text NOT NULL,
  `name` varchar(50) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `start_port` int(11) NOT NULL,
  `end_port` int(11) NOT NULL,
  `open_ports` text NOT NULL,
  `time_taken` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`id`, `date_time`, `name`, `ip`, `start_port`, `end_port`, `open_ports`, `time_taken`) VALUES
(1, 'Sun Feb 26 12:26:49 2023', 'local', '127.0.0.1', 1, 555, '[80, 135, 443, 445]', '2.2079105377197266'),
(2, 'Sun Feb 26 13:09:01 2023', 'db2', '127.0.0.1', 1, 490, '[80, 135, 443, 445]', '2.1660542488098145'),
(3, 'Sun Feb 26 13:10:07 2023', 'okay', '127.0.0.1', 99, 666, '[135, 443, 445]', '2.1880338191986084'),
(4, 'Sun Feb 26 13:11:13 2023', 'finalzz', '127.0.0.1', 66, 1000, '[80, 135, 443, 445]', '2.285796880722046'),
(5, 'Sun Feb 26 13:59:32 2023', 'long test', '127.0.0.1', 0, 65300, '[80, 135, 443, 445, 3306, 5040, 5357, 5354, 6463, 7680, 47937, 49667, 49670, 49668, 49664, 49665, 49666, 55811, 55800, 57621, 58011]', '135.28185057640076'),
(6, 'Sun Feb 26 19:01:52 2023', 'res', '127.0.0.1', 1, 555, '[80, 135, 443, 445]', '2.1932308673858643'),
(7, 'Sun Feb 26 19:02:14 2023', 'res', '127.0.0.1', 1, 555, '[80, 135, 443, 445]', '2.195204734802246'),
(8, 'Sun Feb 26 19:59:42 2023', 'testttGUI', '127.0.0.1', 300, 600, '[443, 445]', '2.17647647857666'),
(9, 'Sun Feb 26 20:13:36 2023', '127.0.0.1', '127.0.0.1', 1, 400, '[80, 135]', '2.152688503265381'),
(10, 'Sun Feb 26 20:15:30 2023', 'testingggg', '127.0.0.1', 430, 900, '[443, 445]', '2.17236590385437'),
(11, 'Sun Feb 26 20:33:50 2023', 'up2', '127.0.0.1', 22, 2200, '[80, 135, 443, 445]', '6.206393003463745'),
(12, 'Mon Feb 27 00:02:20 2023', '12:00', '127.0.0.1', 100, 600, '[135, 443, 445]', '2.1906681060791016'),
(13, 'Mon Feb 27 00:16:36 2023', 'SW', '34.149.36.179', 0, 2000, '[80, 443]', '42.36803579330444'),
(14, 'Mon Feb 27 10:40:24 2023', 'unittest', '127.0.0.1', 1, 500, '[80, 135, 443, 445]', '2.4812817573547363'),
(15, 'Mon Feb 27 10:41:32 2023', 'ut2', '127.0.0.1', 1, 500, '[80, 135, 443, 445]', '2.346879720687866'),
(16, 'Mon Feb 27 10:42:47 2023', 'yt3', '127.0.0.1', 430, 450, '[443, 445]', '2.0611233711242676'),
(17, 'Mon Feb 27 15:58:24 2023', 'test1', '35.186.238.101', 1, 5000, '[80, 443]', '105.58332586288452'),
(18, 'Mon Feb 27 16:01:22 2023', 'SchoolWorksPro', '202.51.74.77', 1, 10000, '[22, 80, 443, 2000, 3307, 5000, 5060, 5432]', '210.824556350708'),
(19, 'Mon Feb 27 16:07:28 2023', 'Softwarica.com', '35.227.194.51', 1, 3000, '[80, 443]', '63.56228971481323');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
