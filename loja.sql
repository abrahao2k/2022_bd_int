create database loja;

use loja;

create table produto(
codigo int primary key auto_increment,
nome varchar(100) not null,
preco float,
estoque int);

