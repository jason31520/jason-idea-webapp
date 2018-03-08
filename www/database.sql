/* add by jason315 2018-3-8 */
drop database if exists jasonidea;
create database jasonidea;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `image` varchar(500) NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_email` (`email`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table blog(
	`id` int(10) NOT NULL AUTO_INCREMENT,
	`user_id` int(10) NOT NULL,
	`user_name` varchar(50) NOT NULL,
	`user_image` varchar(500) NOT NULL,
	`name` varchar(50) NOT NULL,
	`summary` varchar(200) NOT NULL,
	`content` mediumtext NOT NULL,
	`created_at` real NOT NULL,
    KEY `idx_created_at` (`created_at`),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table comment (
    `id` int(10) NOT NULL AUTO_INCREMENT,
    `blog_id` int(10) NOT NULL,
    `user_id` int(10) NOT NULL,
    `user_name` varchar(50) NOT NULL,
    `user_image` varchar(500) NOT NULL,
    `content` mediumtext NOT NULL,
    `created_at` real NOT NULL,
    KEY `idx_created_at` (`created_at`),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;