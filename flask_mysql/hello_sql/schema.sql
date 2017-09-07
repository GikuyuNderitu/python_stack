-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema hello
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hello
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hello` DEFAULT CHARACTER SET utf8 ;
USE `hello` ;

-- -----------------------------------------------------
-- Table `hello`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hello`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- ------------------------------------------------------
-- Prepopulate Tables
-- ------------------------------------------------------
USE `hello`;
-- Users
INSERT INTO `hello`.`users` (`first_name`, `last_name`) VALUES ( 'Boss', 'Hoss');
INSERT INTO `hello`.`users` (`first_name`, `last_name`) VALUES ('Rob', 'Barker');
INSERT INTO `hello`.`users` (`first_name`, `last_name`) VALUES ('Mike', 'Mcguire');
INSERT INTO `hello`.`users` (`first_name`, `last_name`) VALUES ('High', 'Faluten');
INSERT INTO `hello`.`users` (`first_name`, `last_name`) VALUES ('Tina', 'Mckay');
INSERT INTO `hello`.`users` (`first_name`, `last_name`) VALUES ('Lynda', 'Udemy');
INSERT INTO `hello`.`users` (`first_name`, `last_name`) VALUES ('Robert', 'Jones');
