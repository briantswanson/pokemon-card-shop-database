-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: classmysql.engr.oregonstate.edu    Database: cs340_swanbria
-- ------------------------------------------------------
-- Server version	5.5.5-10.6.17-MariaDB-log

-- Brian Swanson & Nick Laustrup
-- Group 98
-- Portfolio Project Step 3 DMQ

# Citation for the following function: SQL DDL
# Date: 5/6/2024
# Copied from /OR/ Adapted from /OR/ Based on 
# Design from Canvas page "Exploration - Database Design Patterns"
# Source URL: https://canvas.oregonstate.edu/courses/1958399/pages/exploration-database-design-patterns?module_item_id=24181801

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
-- Table structure for table `Customers`
-- This table represents a customer entity and contains their contact information.
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customers` (
  `customerID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  PRIMARY KEY (`customerID`),
  UNIQUE KEY `customer_id_UNIQUE` (`customerID`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (1,'Red','Trainer','Red@eliteFour.com','555-555-0001','1234 Card Avenue'),(2,'Ash','Ketchem','pokemon.master@gmail.com','555-555-0002','001 Oak Lab Street'),(3,'Gary','Oak','betterThanAsh@garyoak.com','555-555-0003','002 Oak Lab Street');
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employees`
-- This table represents an employee, unlike a customer, an employee has a wage instead of an address (they are forced to live at the store)
--

DROP TABLE IF EXISTS `Employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employees` (
  `employeeID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `wage` decimal(19,2) NOT NULL,
  PRIMARY KEY (`employeeID`),
  UNIQUE KEY `idEmployees_UNIQUE` (`employeeID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employees`
--

LOCK TABLES `Employees` WRITE;
/*!40000 ALTER TABLE `Employees` DISABLE KEYS */;
INSERT INTO `Employees` VALUES (1,'Brian','Swanson','swanbria@oregonstate.edu','555-555-0004',50.00),(2,'Nick','Laustrup','laustrun@oregonstate.edu','555-555-0005',52.00),(3,'Professor','Oak','oak@pokemonProfessors.com','555-555-0006',100.00);
/*!40000 ALTER TABLE `Employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProductDetails`
-- Product details contains the type of item and name. We chose an enum here since we only sell 3 types of things.
--

DROP TABLE IF EXISTS `ProductDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ProductDetails` (
  `productDetailsID` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) NOT NULL COMMENT 'ENUM = "Snacks", "Cards", "Apparel"\n',
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`productDetailsID`),
  UNIQUE KEY `typeID_UNIQUE` (`productDetailsID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProductDetails`
--

LOCK TABLES `ProductDetails` WRITE;
/*!40000 ALTER TABLE `ProductDetails` DISABLE KEYS */;
INSERT INTO `ProductDetails` VALUES (1,'Cards','Pikachu'),(2,'Snacks','Doritos'),(3,'Apparel','Shop T-Shirt');
/*!40000 ALTER TABLE `ProductDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Products`
-- The products table contains the price, whether the item is in stock, and the details ID from the productDetails table.
--

DROP TABLE IF EXISTS `Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Products` (
  `productID` int(11) NOT NULL AUTO_INCREMENT,
  `price` decimal(19,2) NOT NULL,
  `inStock` tinyint(4) NOT NULL,
  `productDetailsID` int(11) DEFAULT NULL,
  PRIMARY KEY (`productID`),
  UNIQUE KEY `product_id_UNIQUE` (`productID`),
  KEY `productDetailsID_idx` (`productDetailsID`),
  CONSTRAINT `productDetailsID` FOREIGN KEY (`productDetailsID`) REFERENCES `ProductDetails` (`productDetailsID`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products`
--

LOCK TABLES `Products` WRITE;
/*!40000 ALTER TABLE `Products` DISABLE KEYS */;
INSERT INTO `Products` VALUES (10,4.99,1,1),(11,2.99,0,2),(12,10.99,1,3);
/*!40000 ALTER TABLE `Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transactions`
-- The transactions table keeps track of the customer and employee and links to the Transactions_has_Products table
--

DROP TABLE IF EXISTS `Transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transactions` (
  `transactionID` int(11) NOT NULL AUTO_INCREMENT,
  `customerID` int(11) NOT NULL,
  `employeeID` int(11) NOT NULL,
  PRIMARY KEY (`transactionID`,`customerID`,`employeeID`),
  UNIQUE KEY `transaction_id_UNIQUE` (`transactionID`),
  KEY `fk_Transactions_Customers_idx` (`customerID`),
  KEY `fk_Transactions_Employees1_idx` (`employeeID`),
  CONSTRAINT `fk_Transactions_Customers` FOREIGN KEY (`customerID`) REFERENCES `Customers` (`customerID`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_Transactions_Employees1` FOREIGN KEY (`employeeID`) REFERENCES `Employees` (`employeeID`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transactions`
--

LOCK TABLES `Transactions` WRITE;
/*!40000 ALTER TABLE `Transactions` DISABLE KEYS */;
INSERT INTO `Transactions` VALUES (4,1,1),(5,2,2),(6,3,3);
/*!40000 ALTER TABLE `Transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transactions_has_Products`
-- An intersection table that contains the product details of the transaction.
--

DROP TABLE IF EXISTS `Transactions_has_Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transactions_has_Products` (
  `transactionID` int(11) NOT NULL,
  `productID` int(11) NOT NULL,
  PRIMARY KEY (`transactionID`,`productID`),
  KEY `fk_Transactions_has_Products_Products1_idx` (`productID`),
  KEY `fk_Transactions_has_Products_Transactions1_idx` (`transactionID`),
  CONSTRAINT `fk_Transactions_has_Products_Products1` FOREIGN KEY (`productID`) REFERENCES `Products` (`productID`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_Transactions_has_Products_Transactions1` FOREIGN KEY (`transactionID`) REFERENCES `Transactions` (`transactionID`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transactions_has_Products`
--

LOCK TABLES `Transactions_has_Products` WRITE;
/*!40000 ALTER TABLE `Transactions_has_Products` DISABLE KEYS */;
INSERT INTO `Transactions_has_Products` VALUES (1,10),(2,20),(3,30);
/*!40000 ALTER TABLE `Transactions_has_Products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-30 18:19:50
