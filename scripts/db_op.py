# -*- coding:utf-8 -*-

CREATE_DATABASE = '''CREATE DATABASE `minitask`'''

CREATE_TABLE = '''CREATE TABLE `video_info`(
`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
`pic` VARCHAR(255) NOT NULL DEFAULT '',
`mov` INT NOT NULL DEFAULT 0,
`description` VARCHAR(255) NOT NULL DEFAULT ''
,`plays` INT NOT NULL DEFAULT 0,
`create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMPS,
`upper` VARCHAR(255) NOT NULL DEFAULT '',
`duration` INT NOT NULL,
`site_src` VARCHAR(255) NOT NULL DEFAULT ''
)ENGINE=InnoDB CHARSET=utf8'''


CREATE_TABLE_GRAPH = '''CREATE TABLE `regular`(
`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
`period` VARCHAR (255) DEFAULT '',
`col1` int NOT NULL ,
`col2` int NOT NULL ,
`col3` int NOT NULL ,
`col4` int NOT NULL ,
`col5` int NOT NULL ,
`col6` int NOT NULL ,
`col7` int NOT NULL ,
`permutation_order` VARCHAR (14) NOT NULL DEFAULT 0,
`combination_order` VARCHAR (14) NOT NULL DEFAULT 0,
`create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
) ENGINE=InnoDB CHARSET=utf8;
'''