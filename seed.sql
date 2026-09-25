-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: crud-black-clover-crudblackclover.j.aivencloud.com    Database: defaultdb
-- ------------------------------------------------------
-- Server version	8.4.8

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `locais`
--

LOCK TABLES `locais` WRITE;
/*!40000 ALTER TABLE `locais` DISABLE KEYS */;
INSERT INTO `locais` VALUES (1,'Reino de Clover'),(2,'Reino Hearth'),(3,'Reino Spade'),(4,'Reino Diamond'),(5,'País do Sol'),(6,'Floresta das Bruxas');
/*!40000 ALTER TABLE `locais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `racas`
--

LOCK TABLES `racas` WRITE;
/*!40000 ALTER TABLE `racas` DISABLE KEYS */;
INSERT INTO `racas` VALUES (1,'Humano'),(2,'Elfo'),(3,'Anão'),(4,'Demônio');
/*!40000 ALTER TABLE `racas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `espiritos`
--

LOCK TABLES `espiritos` WRITE;
/*!40000 ALTER TABLE `espiritos` DISABLE KEYS */;
INSERT INTO `espiritos` VALUES (1,'Sylph','Vento'),(2,'Salamandra','Fogo'),(3,'Undine','Água'),(4,'Desconhecido','Terra');
/*!40000 ALTER TABLE `espiritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `esquadroes`
--

LOCK TABLES `esquadroes` WRITE;
/*!40000 ALTER TABLE `esquadroes` DISABLE KEYS */;
INSERT INTO `esquadroes` VALUES (1,'Touros Negros',1),(2,'Alvorecer Dourado',1),(3,'Águias de Prata',1),(4,'Rosa Azul',1),(5,'Reis Leões Carmesins',1),(6,'Louva-a-Deus Verdes',1),(7,'Pavões Corais',1),(8,'Órcas Púrpuras',1),(9,'Cervos Cianos',1);
/*!40000 ALTER TABLE `esquadroes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `personagens`
--

LOCK TABLES `personagens` WRITE;
/*!40000 ALTER TABLE `personagens` DISABLE KEYS */;
INSERT INTO `personagens` VALUES (31,'Acier Silva','Aço',3,NULL,1,NULL,1,1,0),(32,'Letoile Becquerel','Bússola',2,NULL,1,NULL,1,1,0),(33,'Sirene Tium','Rocha',2,NULL,1,NULL,1,1,0),(34,'David Swallow','Dado',2,NULL,1,NULL,1,1,0),(35,'En Ringard','Fungo',6,NULL,1,NULL,1,0,0),(36,'Puli Angel','Asas',4,NULL,1,NULL,1,0,0),(37,'Fragil Tormenta','Neve',9,NULL,1,NULL,1,1,0),(38,'Nils Ragus','Gelo',3,NULL,1,NULL,1,1,0),(39,'Ruben Chagar','Areia',5,NULL,1,NULL,1,1,0),(40,'Gueldre Poizot','Transparência',8,NULL,1,NULL,1,0,0),(41,'Xerx Lugner','Gelo',8,NULL,1,NULL,1,1,0),(42,'Damnatio Kira','Balança',NULL,NULL,1,NULL,1,1,0),(43,'Augustus Kira Clover','Luz',NULL,NULL,1,NULL,1,1,0),(44,'Lumiere Silvamillion','Luz',NULL,NULL,1,NULL,1,1,0),(45,'Theresa Rapual','Fogo',NULL,NULL,1,NULL,1,0,0),(46,'Rhya','Imitação',NULL,NULL,2,NULL,1,0,0),(47,'Vetto','Fera',NULL,NULL,2,NULL,1,0,0),(48,'Fana (Elfo)','Cristal',NULL,NULL,2,NULL,1,0,0),(49,'Mars','Cristal',NULL,NULL,1,NULL,4,0,0),(50,'Ladros','Absorção',NULL,NULL,1,NULL,4,0,0),(51,'Lotus Whomalt','Fumaça',NULL,NULL,1,NULL,4,0,0),(52,'Potrof','Planta',NULL,NULL,1,NULL,2,0,0),(53,'Floga','Fogo',NULL,NULL,1,NULL,2,0,0),(54,'Smurik','Vento',NULL,NULL,1,NULL,2,0,0),(55,'Sarado','Terra',NULL,NULL,1,NULL,2,0,0),(56,'Ralph Niaflem','Fogo',NULL,NULL,1,NULL,3,1,0),(57,'Rades Spirito','Espectro',NULL,NULL,1,NULL,1,0,0),(58,'Valtos','Portal Espacial',NULL,NULL,1,NULL,1,0,0),(59,'Sally','Gel',NULL,NULL,1,NULL,1,0,0),(60,'Neige','Neve',NULL,NULL,1,NULL,1,0,0),(61,'Asta','Anti-Magia',1,NULL,1,NULL,1,0,1),(62,'Yuno','Vento',2,1,1,2,1,1,0),(63,'Noelle Silva','Água',1,3,1,NULL,1,1,0),(64,'Yami Sukehiro','Trevas',1,NULL,1,NULL,5,0,0),(65,'Luck Voltia','Relâmpago',1,NULL,1,NULL,1,0,0),(66,'Magna Swing','Chama',1,NULL,1,NULL,1,0,0),(67,'Charmy Pappitson','Algodão/Comida',1,NULL,1,4,1,0,0),(68,'Gauche Adlai','Espelho',1,NULL,1,NULL,1,0,0),(69,'Vanessa Enoteca','Fio do Destino',1,NULL,1,NULL,6,0,0),(70,'Finral Roulacase','Portal Espacial',1,NULL,1,NULL,1,1,0),(71,'Gordon Agrippa','Veneno',1,NULL,1,NULL,1,0,0),(72,'Grey','Transformação',1,NULL,1,NULL,1,0,0),(73,'Zora Ideale','Magia de Armadilha',1,NULL,1,NULL,1,0,0),(74,'Henry Legolant','Recombinação',1,NULL,1,NULL,1,0,0),(75,'Nero (Secre)','Selamento',1,NULL,1,NULL,1,0,0),(76,'William Vangeance','Mundo',2,NULL,1,2,1,1,0),(77,'Mimosa Vermillion','Planta',2,NULL,1,NULL,1,1,0),(78,'Klaus Lunettes','Criação de Aço',2,NULL,1,NULL,1,0,0),(79,'Langris Vaude','Portal Espacial',2,NULL,1,NULL,1,1,0),(80,'Fuegoleon Vermillion','Fogo',5,2,1,NULL,1,1,0),(81,'Mereoleona Vermillion','Fogo',5,NULL,1,NULL,1,1,0),(82,'Leopold Vermillion','Fogo',5,NULL,1,NULL,1,1,0),(83,'Charlotte Roselei','Magia de Espinhos',4,NULL,1,NULL,1,1,0),(84,'Sol Marron','Magia do Solo',4,NULL,1,NULL,1,0,0),(85,'Nozel Silva','Mercúrio',3,NULL,1,NULL,1,1,0),(86,'Nebra Silva','Névoa',3,NULL,1,NULL,1,1,0),(87,'Solid Silva','Água',3,NULL,1,NULL,1,1,0),(88,'Jack the Ripper','Magia de Corte',6,NULL,1,NULL,1,0,0),(89,'Sekke Bronzazza','Magia de Bronze',6,NULL,1,NULL,1,0,0),(90,'Dorothy Unsworth','Magia do Sonho',7,NULL,1,NULL,1,1,0),(91,'Kirsch Vermillion','Magia de Cerejeira',7,NULL,1,NULL,1,1,0),(92,'Kaiser Granvorka','Vórtice',8,NULL,1,NULL,1,1,0),(93,'Rill Boismortier','Pintura',9,NULL,1,NULL,1,0,0),(94,'Licht','Espadas',NULL,NULL,2,NULL,1,0,0),(95,'Patry','Luz',NULL,NULL,2,NULL,1,0,0),(96,'Zagred','Palavra Mágica',NULL,NULL,3,NULL,1,0,1),(97,'Dante Zogratis','Gravidade',NULL,NULL,1,NULL,3,0,1),(98,'Vanica Zogratis','Sangue',NULL,NULL,1,NULL,3,0,1),(99,'Zenon Zogratis','Osso',NULL,NULL,1,NULL,3,0,1),(101,'Gaja','Relâmpago',NULL,NULL,1,NULL,2,0,0),(102,'Lolopechka','Água',NULL,3,1,NULL,2,1,0),(103,'Julius Novachrono','Tempo',NULL,NULL,1,NULL,1,0,0),(104,'Marx Francois','Magia de Memória',NULL,NULL,1,NULL,1,0,0),(105,'Owen','Cura',NULL,NULL,1,NULL,1,0,0);
/*!40000 ALTER TABLE `personagens` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-24 20:15:41
