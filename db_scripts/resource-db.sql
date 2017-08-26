# Database for resources
CREATE USER IF NOT EXISTS `resource_user`@`localhost` IDENTIFIED BY 'password';

CREATE DATABASE IF NOT EXISTS `resource-db`;

GRANT ALL PRIVILEGES ON `resource-db` TO `resource_user`@`localhost`;

USE `resource-db`;

CREATE TABLE IF NOT EXISTS `resources` (
  resource_id int(10) auto_increment,
  resource_string varchar(50),
  primary key (resource_id)
);

GRANT ALL PRIVILEGES ON `resources` TO `resource_user`@`localhost`;

INSERT INTO `resources` (resource_string) VALUES ('resource 1: secret 1');

INSERT INTO `resources` (resource_string) VALUES ('resource 2: secret 2');