CREATE DATABASE balancemaster;

create table test720(
    id integer(10) primary key auto_increment,
    username varchar(30) not null,
    email varchar(255) not null default 'johndoe@gmail.com',
    password varchar(255) not null  
);

INSERT INTO test720 (username,password) VALUES("johndoe","1234");