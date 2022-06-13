show databases; 
create database administracion;
show tables;
create table usuarios(
	nombre varchar(30),
	clave varchar(10)
);
describe usuarios;
desc usuarios;
drop table if exists usuarios;
insert into usuarios (nombre, clave) values ("MarioPerez","Mario");
create table libros(
	titulo varchar(40),
	autor varchar(20),
	editorial varchar(15),
	precio float,
	cantidad integer
);
describe libros;
show tables;

insert into libros (titulo,autor,editorial,precio)
values('El aleph','Borges','Planeta',15);
insert into libros (titulo,autor,editorial,precio)
values('Martin Fierro','Jose Hernandez','Emece',22.20);
insert into libros (titulo,autor,editorial,precio)
values('Antologia poetica','Borges','Planeta',40);
insert into libros (titulo,autor,editorial,precio)
values('Aprenda PHP','Mario Molina','Emece',18.20);
insert into libros (titulo,autor,editorial,precio)
values('Cervantes y el quijote','Borges','Paidos',36.40);
insert into libros (titulo,autor,editorial,precio)
values('Manual de PHP', 'J.C. Paez', 'Paidos',30.80);
insert into libros (titulo,autor,editorial,precio)
values('Harry Potter y la piedra filosofal','J.K. Rowling','Paidos',45.00);
insert into libros (titulo,autor,editorial,precio)
values('Harry Potter y la camara secreta','J.K. Rowling','Paidos',46.00);
insert into libros (titulo,autor,editorial,precio)
values('Alicia en el pais de las maravillas','Lewis Carroll','Paidos',null);

select * from libros;

select titulo, autor, editorial from libros;

select nombre, clave from usuarios where nombre="MarioPerez";

drop table if exists usuarios;
create table usuarios (
	nombre varchar(30),
    clave varchar(10)
);
desc usuarios;

insert into usuarios values('Federico','455');
insert into usuarios values('Gonzalo','55');
insert into usuarios values('Andrea','4');
insert into usuarios values('Marta','435');
insert into usuarios values('Federico','25');
insert into usuarios values('Juan','15');

select * from usuarios;

delete from usuarios;

delete from usuarios where nombre="Federico";

update usuarios set clave="RealMadrid";

update usuarios set nombre="Mario" where nombre="Gonzalo"; 

update usuarios set nombre="MarceloDuarte", clave="Marce" where nombre="Juan";

select * from libros limit 0,4;

select * from libros limit 5,4;

delete from libros limit 2;

select * from libros order by precio limit 2;

select * from libros where titulo="El aleph" and autor="Borges" and editorial="Planeta";

select * from libros;