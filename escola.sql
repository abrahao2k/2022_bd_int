create database escola;

use escola;

create table aluno(
codigo int primary key auto_increment,
nome varchar(100) not null,
curso varchar(100)
);

insert into aluno values(1,"Ana","Informática");
insert into aluno values(2,"Breno","Mecânica");
insert into aluno values(3,"Clara","Edificações");
insert into aluno values(4,"Diego","Eletrotécnica");
