create table if not exists `users` (
    `name` varchar(50) not null,
    `email` varchar(50) not null unique,
    `password` varchar(50) not null,

    primary key (`email`)
);

INSERT INTO `users` (`name`, `email`, `password`) VALUES ('Admin','admin@gmail.com','admin');
INSERT INTO `users` (`name`, `email`, `password`) VALUES ('Oscar','oalvarezr@unal.edu.co','password');
