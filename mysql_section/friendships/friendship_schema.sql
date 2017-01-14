-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema friendships
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friendships
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friendships` DEFAULT CHARACTER SET utf8 ;
USE `friendships` ;

-- -----------------------------------------------------
-- Table `friendships`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendships`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT
  `last_name` VARCHAR(45) NOT
  `created_at` DATETIME
  `updated_at` DATETIME
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendships`.`friendships`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendships`.`friendships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT
  `friend_id` INT NOT
  `created_at` DATETIME
  `updated_at` DATETIME
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- ------------------------------------------------------
-- Prepopulate Tables
-- ------------------------------------------------------
-- Users
INSERT INTO `friendships`.`users` (`first_name`, `last_name`) VALUES ( 'Boss', 'Hoss');
INSERT INTO `friendships`.`users` (`first_name`, `last_name`) VALUES ('Rob', 'Barker');
INSERT INTO `friendships`.`users` (`first_name`, `last_name`) VALUES ('Mike', 'Mcguire');
INSERT INTO `friendships`.`users` (`first_name`, `last_name`) VALUES ('High', 'Faluten');
INSERT INTO `friendships`.`users` (`first_name`, `last_name`) VALUES ('Tina', 'Mckay');
INSERT INTO `friendships`.`users` (`first_name`, `last_name`) VALUES ('Lynda', 'Udemy');
INSERT INTO `friendships`.`users` (`first_name`, `last_name`) VALUES ('Robert', 'Jones');

-- Friendships
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('1', '3');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('2', '4');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('4', '2');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('3', '1');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('7', '5');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('7', '1');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('1', '7');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('5', '7');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('2', '5');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('5', '2');
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`) VALUES ('7', '4');
