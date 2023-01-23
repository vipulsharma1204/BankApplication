-- ---------------------------------------------------------------------------------------- --
drop database bank;
create database bank;
use bank;
drop table `home_bankusers`;
CREATE TABLE `home_bankusers` (
  `username` varchar(16) NOT NULL,
  `password` varchar(128) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
drop table `home_creditrecord`;
CREATE TABLE `home_creditrecord` (
  `accountNumber` bigint NOT NULL,
  `dateoftransac` datetime NOT NULL,
  `amount` bigint NOT NULL,
  PRIMARY KEY (`accountNumber`),
  UNIQUE KEY `accountNumber_UNIQUE` (`accountNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
drop table `home_debitrecord`;
CREATE TABLE `home_debitrecord` (
  `accountNumber` bigint NOT NULL,
  `dateoftransac` datetime NOT NULL,
  `amount` bigint NOT NULL,
  PRIMARY KEY (`accountNumber`),
  UNIQUE KEY `accountNumber_UNIQUE` (`accountNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
drop table `home_signupdetails`;
CREATE TABLE `home_signupdetails` (
  `username` varchar(128) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `email` varchar(128) NOT NULL,
  `address` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phoneNumber` varchar(14) NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `phoneNumber_UNIQUE` (`phoneNumber`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
DROP TABLE `home_userdetail`;
CREATE TABLE `home_userdetail` (
  `username` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `address` varchar(200) NOT NULL,
  `phoneNumber` bigint NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `middleName` varchar(50) DEFAULT NULL,
  `motherName` varchar(50) NOT NULL,
  `fatherName` varchar(50) NOT NULL,
  `alternatePhoneNumber` varchar(14) DEFAULT NULL,
  `dateOfBirth` datetime(6) NOT NULL,
  `zipCode` int NOT NULL,
  `aadhaarNumber` bigint NOT NULL,
  `occupation` varchar(50) NOT NULL,
  `relation` varchar(50) NOT NULL,
  `accountType` varchar(50) NOT NULL,
  `password` varchar(150) NOT NULL,
  `namePrefix` datetime(6) NOT NULL,
  `panNhome_userdetailumber` varchar(10) NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  `accountNumber` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `phoneNumber_UNIQUE` (`phoneNumber`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `accountNumber_UNIQUE` (`accountNumber`),
  UNIQUE KEY `panNumber_UNIQUE` (`panNumber`),
  UNIQUE KEY `aadhaarNumber_UNIQUE` (`aadhaarNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ---------------------------------------------------------------------------------------- --
