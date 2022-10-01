-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_ninjas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojos_ninjas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_ninjas` DEFAULT CHARACTER SET utf8 ;
USE `dojos_ninjas` ;

-- -----------------------------------------------------
-- Table `dojos_ninjas`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_ninjas`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(156) NULL,
  `creado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_ninjas`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_ninjas`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(64) NULL,
  `apellido` VARCHAR(64) NULL,
  `edad` INT NULL,
  `email` VARCHAR(156) NULL,
  `creado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dojos_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojos_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojos_id`)
    REFERENCES `dojos_ninjas`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
