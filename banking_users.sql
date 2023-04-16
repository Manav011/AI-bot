-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: banking
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `acc_no` varchar(20) NOT NULL,
  `mobile_no` varchar(10) NOT NULL,
  `email` varchar(320) DEFAULT NULL,
  `dob` date NOT NULL,
  `address` varchar(200) NOT NULL,
  `acc_type` varchar(20) NOT NULL,
  `acc_status` varchar(15) NOT NULL,
  `acc_activation_date` date NOT NULL,
  `total_bal` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `acc_no` (`acc_no`),
  UNIQUE KEY `mobile_no` (`mobile_no`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Raju Reddy','150325482515487','9854261456','raju@gmail.com','1986-04-11','7-81, Chennai, Seruseri, Tamilnadu','Savings','Active','2003-04-26',10200),(2,'Vamsi Krishna','554418556692145','9854261463','vamsi@gmail.com','1990-04-11','3-71, Lucknow, Uttar Pradesh','Current','Inactive','2005-02-05',54800),(3,'Naveen Reddy','883091452100564','9854261496','naveen@gmail.com','1985-03-14','5-81, MG Road, Bangalore, Karnataka','Savings','Active','2001-09-10',540800),(4,'Raghava Rao','889947556632115','9854261412','raghava@gmail.com','1985-09-21','4-81, Iroli, Mumbai, Maharashtra','Fixed Deposit','Active','2001-09-10',9800),(5,'Harsha Vardhan','221548869547521','9854261445','harsha@gmail.com','1992-10-11','6-81, Street1, Ahemadabad, Gujarat','Current','Active','2005-05-12',103900),(6,'Sapna Chowdary','7758442010336201','9898521010','sapna@gmail.com','1998-06-24','9-21, Sholinganur, Chennai, Tamilnadu','Current','Suspended','2007-08-04',1900),(7,'Simran Sharma','556488953212662','8841056131','simran@gmail.com','2000-09-30','6-21, Ambedkar Street, Hyderabad, Andhra Pradesh','Savings','Active','2010-07-12',50000),(8,'Arun Khan','6620152485209630','7745962210','arun@gmail.com','2001-10-15','5-42, New Street, Saharanpur, Uttar Pradesh','Savings','Active','2011-07-08',60500),(9,'Rehan Dhawan','965478542100152','9962116320','rehan@gmail.com','1990-06-20','81, Mall Road, Shimla, Himachal Pradesh','Current','Active','2004-11-09',600580),(10,'Shikha Aggarwal','775469326544521','6678542189','shikha@gmail.com','1988-12-16','4, Street5 , Rishikesh, Uttarakhand','Savings','Active','2001-06-15',810900);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-16 13:49:43
