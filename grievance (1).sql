-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 23, 2024 at 07:38 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `grievance`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_db`
--

CREATE TABLE `admin_db` (
  `id` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_db`
--

INSERT INTO `admin_db` (`id`, `username`, `password`) VALUES
(1, 'chauhan', 777);

-- --------------------------------------------------------

--
-- Table structure for table `catagories`
--

CREATE TABLE `catagories` (
  `id` int(255) NOT NULL,
  `categories_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `catagories`
--

INSERT INTO `catagories` (`id`, `categories_name`) VALUES
(8, 'WATER'),
(9, 'FOOD'),
(10, 'INTERNET'),
(11, 'CLEANING'),
(12, 'OTHERS');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `id` int(255) NOT NULL,
  `course_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`id`, `course_name`) VALUES
(17, 'BCA'),
(19, 'MCA\r\n'),
(20, 'BBA'),
(21, 'MTECH\r\n'),
(22, 'BTECH'),
(23, 'BA'),
(24, 'MA'),
(25, 'MBA');

-- --------------------------------------------------------

--
-- Table structure for table `grievance_model`
--

CREATE TABLE `grievance_model` (
  `id` int(255) NOT NULL,
  `course_id` varchar(255) NOT NULL,
  `categories_id` varchar(255) NOT NULL,
  `room_id` varchar(255) NOT NULL,
  `complaint` varchar(255) NOT NULL,
  `status` int(255) NOT NULL DEFAULT 0,
  `date` date DEFAULT current_timestamp(),
  `student_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `grievance_model`
--

INSERT INTO `grievance_model` (`id`, `course_id`, `categories_id`, `room_id`, `complaint`, `status`, `date`, `student_id`) VALUES
(7, 'BCA', 'Water', '101', 'Not drinkable', 2, '2024-06-21', 2),
(8, 'BCA', 'Water', '103', 'yjghd', 1, '2024-06-21', 2),
(9, 'BCA', 'Water', 'INTERNET', 'VERY POOR', 1, '2024-06-22', 2),
(10, 'BCA', 'Water', '103', 'In Library', 2, '2024-06-22', 2),
(11, 'BCA', 'Water', '55', 'jd', 2, '2024-06-22', 2),
(12, 'BCA', 'Water', '454', 'rtyhastsz', 2, '2024-06-22', 2),
(13, 'BCA', 'Water', '525', 'i87tfg8i', 2, '2024-06-22', 2),
(14, 'BCA', 'Water', '101', 'sfh', 0, '2024-06-22', 1),
(15, 'BCA', 'Water', '101', 'yufyhj', 2, '2024-06-22', 1),
(16, 'BCA', 'Water', '454', 'rthgwstgh', 2, '2024-06-25', 2),
(17, 'BCA', 'Water', '010', 'gjkl', 1, '2024-06-25', 1),
(18, 'BCA', 'Water', '7', 'oiuy', 2, '2024-06-25', 1),
(19, '2', '2', '52', 'ryf7u', 2, '2024-06-26', 1),
(20, 'MCA', 'Lack of Resources', '52', 'dfh', 2, '2024-06-26', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user_db`
--

CREATE TABLE `user_db` (
  `id` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `student_roll_no` int(255) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_db`
--

INSERT INTO `user_db` (`id`, `username`, `password`, `email`, `student_roll_no`, `status`) VALUES
(1, 'radhe', '777', 'radheradhe@email.com', 33, 1),
(2, 'govind', '333', 'govind@123', 21, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_db`
--
ALTER TABLE `admin_db`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `catagories`
--
ALTER TABLE `catagories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `grievance_model`
--
ALTER TABLE `grievance_model`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_db`
--
ALTER TABLE `user_db`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_db`
--
ALTER TABLE `admin_db`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `catagories`
--
ALTER TABLE `catagories`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `grievance_model`
--
ALTER TABLE `grievance_model`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `user_db`
--
ALTER TABLE `user_db`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
