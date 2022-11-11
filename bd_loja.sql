create database loja;

use loja;

create table produto(
codigo int primary key auto_increment,
nome varchar(100),
preco float,
estoque float);

insert into produto values
(null,"teclado", 99, 6),
(null, "mouse", 49, 8), 
(null, "headphone", 250, 3),
(null, "cadeira gamer", 1400, 1),
(null, "controle xbox", 450, 2);