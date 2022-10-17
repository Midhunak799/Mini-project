/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - club management system1
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`club management system1` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `club management system1`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `reviews` varchar(20) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`f_id`),
  KEY `user id` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(28) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(10) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'midhun','123','admin'),
(15,'dhoni','dhoni1234','user');

/*Table structure for table `membership` */

DROP TABLE IF EXISTS `membership`;

CREATE TABLE `membership` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `user id` int(11) NOT NULL,
  `date` date NOT NULL,
  `paymentstatus` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `membership` */

/*Table structure for table `news` */

DROP TABLE IF EXISTS `news`;

CREATE TABLE `news` (
  `Newsid` int(10) NOT NULL AUTO_INCREMENT,
  `Newstitle` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `details` varchar(100) NOT NULL,
  PRIMARY KEY (`Newsid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `news` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment id` int(11) NOT NULL AUTO_INCREMENT,
  `user id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `payment date` date NOT NULL,
  PRIMARY KEY (`payment id`),
  KEY `user id` (`user id`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`user id`) REFERENCES `registration` (`user id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `registration` */

DROP TABLE IF EXISTS `registration`;

CREATE TABLE `registration` (
  `user id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'registration id for user',
  `login_id` int(10) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `gender` varchar(90) NOT NULL,
  `dob` date NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Phoneno` varchar(15) NOT NULL,
  PRIMARY KEY (`user id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `registration` */

insert  into `registration`(`user id`,`login_id`,`Name`,`Address`,`gender`,`dob`,`Email`,`Phoneno`) values 
(13,15,'MS DHONI','RANCHI','Male','1981-07-07','msdhoni7@gmail.com','8198987623');

/*Table structure for table `sports` */

DROP TABLE IF EXISTS `sports`;

CREATE TABLE `sports` (
  `sports id` int(11) NOT NULL AUTO_INCREMENT,
  `sports categories` varchar(20) NOT NULL,
  `detils` varchar(50) NOT NULL,
  PRIMARY KEY (`sports id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `sports` */

/*Table structure for table `sportsresults` */

DROP TABLE IF EXISTS `sportsresults`;

CREATE TABLE `sportsresults` (
  `rsult id` int(11) NOT NULL AUTO_INCREMENT,
  `tournament id` int(11) NOT NULL,
  `team1` varchar(20) DEFAULT NULL,
  `team2` varchar(20) DEFAULT NULL,
  `result` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`rsult id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `sportsresults` */

/*Table structure for table `tournaments` */

DROP TABLE IF EXISTS `tournaments`;

CREATE TABLE `tournaments` (
  `tournament id` int(11) NOT NULL,
  `sports id` int(11) NOT NULL AUTO_INCREMENT,
  `tornament name` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `details` varchar(50) NOT NULL,
  PRIMARY KEY (`tournament id`),
  KEY `sports id` (`sports id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tournaments` */

/*Table structure for table `tourrnamentreg` */

DROP TABLE IF EXISTS `tourrnamentreg`;

CREATE TABLE `tourrnamentreg` (
  `team id` int(11) NOT NULL,
  `tournament id` int(11) NOT NULL AUTO_INCREMENT,
  `team name` varchar(20) NOT NULL,
  `phone no` varchar(15) NOT NULL,
  PRIMARY KEY (`team id`),
  KEY `tournament id` (`tournament id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tourrnamentreg` */

/*Table structure for table `upcoming events` */

DROP TABLE IF EXISTS `upcoming events`;

CREATE TABLE `upcoming events` (
  `eventid` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id for upcoming events',
  `eventname` varchar(20) NOT NULL COMMENT 'name of upcoming events',
  `date` date NOT NULL COMMENT 'date of events',
  `details` varchar(50) NOT NULL COMMENT 'details of events',
  PRIMARY KEY (`eventid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `upcoming events` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
