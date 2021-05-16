create database OrgVy;
use OrgVy;

create table if not exists `type` (
	`id` int not null auto_increment,
    `name` varchar(50) not null unique,
    primary key (`id`)
);

create table if not exists `category` (
	`id` int not null auto_increment,
    `name` varchar(50) not null unique,
    primary key (`id`)
);

create table if not exists `Audiovisual` (
	`id` int not null auto_increment,
    `name` varchar(50) not null unique,
    `image` blob ,
    `type` varchar(50) not null,
    `categories` varchar(50) not null,
    `score` int not null,
    primary key (`id`),
    constraint foreign key (`type`) references `type` (`name`) on delete no action on update no action,
    constraint foreign key (`categories`) references `category` (`name`) on delete no action on update no action
);

INSERT INTO `OrgVy`.`type` (`name`) VALUES ('Anime');
INSERT INTO `OrgVy`.`type` (`name`) VALUES ('Serie');
INSERT INTO `OrgVy`.`type` (`name`) VALUES ('Pelicula');
INSERT INTO `OrgVy`.`type` (`name`) VALUES ('Libro');
INSERT INTO `OrgVy`.`type` (`name`) VALUES ('Novela');

INSERT INTO `OrgVy`.`category` (`name`) VALUES ('Romance');
INSERT INTO `OrgVy`.`category` (`name`) VALUES ('Gore');
INSERT INTO `OrgVy`.`category` (`name`) VALUES ('Fantasia');
INSERT INTO `OrgVy`.`category` (`name`) VALUES ('Psicologico');
INSERT INTO `OrgVy`.`category` (`name`) VALUES ('C. Ficcion');
INSERT INTO `OrgVy`.`category` (`name`) VALUES ('Drama');
INSERT INTO `OrgVy`.`category` (`name`) VALUES ('Comedia');
INSERT INTO `OrgVy`.`category` (`name`) VALUES ('Ecchi');
