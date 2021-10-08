-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 07, 2021 at 06:35 AM
-- Server version: 8.0.26-0ubuntu0.20.04.2
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fayaz`
--
CREATE DATABASE IF NOT EXISTS `fayaz` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `fayaz`;

-- --------------------------------------------------------

--
-- Table structure for table `aboutme`
--

CREATE TABLE IF NOT EXISTS `aboutme` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `skill` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `bio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `country` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `image` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'myimg.jpg',
  `address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `city` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `zip` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `aboutme`
--

INSERT INTO `aboutme` (`id`, `uid`, `skill`, `bio`, `country`, `image`, `address`, `city`, `zip`) VALUES
(2, 1, 'FLASK EXPERT', 'I\'m A web designer & front‑end developer focused on crafting clean & user‑friendly experiences, I am passionate about building excellent web applications. Welcome to my Website. I am a web developer striving my best to provide you with an unusual experience with flask, python. Some technologies never fade, Web development is one of those technologies.None', 'Pakistan', 'nzpBKG-5RDBZlZIJa3-_IRxJkp8.jpg', 'A One City brewery', 'Quetta', '87300'),
(5, 3, 'PROGRAMMER', 'Credibly embrace visionary internal or \"organic\" sources and business benefits. Collaboratively\r\nintegrate efficient portals rather than customized customer service. Assertively deliver\r\nfrictionless services via leveraged interfaces. Conveniently evisculate accurate sources and\r\nprocess-centric expertise. Energistically fabricate customized imperatives through cooperative\r\ncatalysts for change.', 'Pakistan', 'ir2hS7pGahC1WpislFOhBPfpPT0.jpg', 'Main Bazar', 'Awaran', '87300'),
(7, 7, 'WEB DESIGNER', 'hshshsh', 'dhhdhd', 'QxJPhVzHFwaOK1FdiqkgTaOY9hM.jpg', 'hdhdh', 'dhhdh', '444'),
(8, 9, 'PROGRAMMER', 'DJJDJDJ', 'Pakistan', 'nH1ZgsaXFzrwjEMbQJj4mkCvJxs.jpg', 'A One City', 'quetta', '87300'),
(9, 11, 'ENTERPREUNER', 'I am a public famous author', 'Pakistan', 'vP51PqTxGjMXaH5XqsV6D5quY8A.jpg', 'A One City', 'quetta', '87300'),
(10, 13, 'WEB DESIGNER', 'I am a social activist', 'Pakistan', '91yV95r-9i_S7Np1X6qDpWS2H0w.jpg', 'UOB', 'Hub Chowki', '83000');

-- --------------------------------------------------------

--
-- Table structure for table `education`
--

CREATE TABLE IF NOT EXISTS `education` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `certificate_name` varchar(300) NOT NULL,
  `institute` varchar(300) NOT NULL,
  `about` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `s_date` varchar(100) NOT NULL,
  `e_date` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `education`
--

INSERT INTO `education` (`id`, `uid`, `certificate_name`, `institute`, `about`, `s_date`, `e_date`) VALUES
(1, 1, 'BS (IT)', 'University of Balochistan', 'The University of Balochistan, also known as Balochistan University, is a public university located in the downtown area of Quetta, Balochistan, Pakistan. UoB is the oldest highest education institution in Balochistan, having been established in 1970.', '2017', '2021'),
(2, 1, 'BS IT', 'University of Balochistan', 'SARYAB ROAD', '2017', '2021'),
(3, 12, 'BS(IT)', 'BS(IT)', 'BS(IT)', 'BS(IT)', 'BS(IT)'),
(4, 12, 'BS(IT)', 'UNIVERSITY OF BALOCHISTAN', 'nothing', '2018', '2022'),
(5, 12, 'INTERMEDIATE', 'BBISE, QUETTA', 'KSKJSKLCL SJHJKD', '19999', '11883'),
(6, 12, 'INTERMEDIATE', 'BBISE, QUETTA', 'sbcj djshjs', '199992', '199222'),
(7, 12, 'BS(IT)', 'BBISE, QUETTA', 'mnsdn jdshsdjhd', '19993', '19222'),
(8, 12, 'BS(IT)', 'BBISE, QUETTA', 'mnsdn jdshsdjhd', '19993', '19222');

-- --------------------------------------------------------

--
-- Table structure for table `expertise`
--

CREATE TABLE IF NOT EXISTS `expertise` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `exp_name` varchar(100) NOT NULL,
  `exp_info` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `expertise`
--

INSERT INTO `expertise` (`id`, `uid`, `exp_name`, `exp_info`) VALUES
(1, 1, 'WEB DEVELOPMENT', 'I am a professional Web developer with 4 years of Experience '),
(2, 1, 'PHOTOSHOP DESIGNER', 'This series of videos introduces basic Photoshop design techniques. You\'ll learn how to work with layers, combine images, use layer masks, ...'),
(4, 3, 'PYTHON PROGRAMING', 'I am a programmer');

-- --------------------------------------------------------

--
-- Table structure for table `interest`
--

CREATE TABLE IF NOT EXISTS `interest` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `int_name` varchar(200) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `interest`
--

INSERT INTO `interest` (`id`, `uid`, `int_name`, `description`) VALUES
(1, 1, 'BOOKS', 'Proactively extend market-driven e-tailers rather than enterprise-wide supply chains. Collaboratively embrace 24/7 processes rather than adaptive users. Seamlessly monetize alternative e-business.'),
(2, 1, 'Sports', 'Assertively grow optimal methodologies after viral technologies. Appropriately develop\r\nfrictionless technology for adaptive functionalities. Competently iterate functionalized\r\nnetworks for best-of-breed services.'),
(3, 1, 'Art', 'Dramatically utilize superior infomediaries whereas functional core competencies.\r\nEnthusiastically repurpose synergistic vortals for customer directed portals. Interactively\r\npursue sustainable leadership via.'),
(4, 3, 'BOOKS', 'Proactively extend market-driven e-tailers rather than enterprise-wide supply chains. Collaboratively embrace 24/7 processes rather than adaptive users. Seamlessly monetize alternative e-business.'),
(5, 3, 'Sports', 'Assertively grow optimal methodologies after viral technologies. Appropriately develop\r\nfrictionless technology for adaptive functionalities. Competently iterate functionalized\r\nnetworks for best-of-breed services.'),
(6, 3, 'Art', 'Dramatically utilize superior infomediaries whereas functional core competencies.\r\nEnthusiastically repurpose synergistic vortals for customer directed portals. Interactively\r\npursue sustainable leadership via.');

-- --------------------------------------------------------

--
-- Table structure for table `skills`
--

CREATE TABLE IF NOT EXISTS `skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `skill_name` varchar(300) NOT NULL,
  `percentage` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `skills`
--

INSERT INTO `skills` (`id`, `uid`, `skill_name`, `percentage`) VALUES
(1, 1, 'Marketing', 88),
(2, 1, 'Market Research', 20),
(3, 1, 'Organisational Skills', 99),
(9, 1, 'Project Management', 84),
(10, 13, 'WEB DESIGNER', 10);

-- --------------------------------------------------------

--
-- Table structure for table `social`
--

CREATE TABLE IF NOT EXISTS `social` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `facebook` varchar(40) NOT NULL,
  `twitter` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `instagram` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `github` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `youtube` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `social`
--

INSERT INTO `social` (`id`, `uid`, `facebook`, `twitter`, `instagram`, `github`, `youtube`) VALUES
(1, 1, 'wali.kubdani', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `password` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `email`, `phone`, `password`) VALUES
(1, 'Wali Baloch', 'walikubdani', 'iscobaloch@gmail.com', '03083702100', '123456789'),
(2, 'WALI', 'waliii', 'wali@gmail.com', '73737373', '111111'),
(3, 'Fayaz GN', 'fayazgn', 'fayazgn23@gmail.com', '9838383838', 'fayazgn'),
(4, '', '', '', '777776766767', ''),
(5, 'wali', 'dddd', 'wali@gmail.com', '36666666666', '122111221'),
(6, 'Hammad Malik', 'hammad', 'hammad.malik17@gmail.com', '03440800372', 'hammad'),
(7, 'Haris Haider', 'haris', 'haris@gmail.com', '03355454545', 'haris1'),
(8, 'dhdjhd', 'djdhdjh', 'dhgdh@gghhg.com', '72882392398', 'hdddh'),
(9, 'Usama', 'usama', 'usama@gmail.com', '98383883811', 'usama11'),
(11, 'Zamran Baloch', 'zamran', 'zamran@gmail.com', '88888888888', 'zamran'),
(12, 'Wali Baloch', 'isco22', 'iscokubdani@gmail.com', '03083702100', '121212'),
(13, 'GHULAM RASOOL', 'grazad', 'grazad@gmail.com', '87873383843', '121212');

-- --------------------------------------------------------

--
-- Table structure for table `work_experience`
--

CREATE TABLE IF NOT EXISTS `work_experience` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `design` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `organization` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `about` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `s_date` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `e_date` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `work_experience`
--

INSERT INTO `work_experience` (`id`, `uid`, `design`, `organization`, `about`, `s_date`, `e_date`) VALUES
(1, 2, 'HEAD OF MARKET RESEARCH', 'A&B Business ', 'United Kingdom, London', '2019', 'present'),
(8, 2, 'lecturer', 'University of Balochistan', 'jjdjdndjndj', '2018', 'Present'),
(9, 1, 'DB ADMIN', 'UNKNOWN', 'worked as db data entry', '2018', 'PRESENT');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
