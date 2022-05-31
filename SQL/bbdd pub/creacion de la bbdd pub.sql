create database if not exists pub; 

use pub;

create table if not exists pub (
COD_PUB int primary key not null auto_increment,
NOMBRE varchar(25),
LICENCIA_FISCAL varchar(25),
DOMICILIO varchar(25),
FECHA_APERTURA date,
HORARIO varchar(25),
COD_LOCALIDAD int);

create table if not exists titular (
DNI_TITULAR int primary key not null auto_increment,
NOMBRE varchar(25),
DOMICILIO varchar(25),
COD_PUB int);

create table if not exists empleado (
DNI_EMPLEADO int primary key not null auto_increment,
NOMBRE varchar(25),
DOMICILIO varchar(25));

create table if not exists localidad (
COD_LOCALIDAD int primary key not null auto_increment,
NOMBRE varchar(25));

create table if not exists existencias (
COD_ARTICULO int primary key not null auto_increment,
NOMBRE varchar(25),
CANTIDAD int,
PRECIO int,
COD_PUB int);

create table if not exists pub_empleado (
COD_PUB int not null,
DNI_EMPLEADO int not null,
FUNCION varchar(25) not null,
primary key (COD_PUB, DNI_EMPLEADO, FUNCION));

insert into localidad (COD_LOCALIDAD, NOMBRE) 
values 
("01","Barcelona"),("02","Hospitalet"),("03","Barceloneta"),("04","Florida");

insert into pub (NOMBRE, LICENCIA_FISCAL, DOMICILIO, FECHA_APERTURA, HORARIO, COD_LOCALIDAD) 
values 
("Pub verde", "asd456", "calle uno 23", "2021-05-12", "21", "01"),
("Pub rojo", "qwe485", "calle dos 52", "2020-02-01", "21", "01"),
("Pub azul", "bvc458", "calle tres 96", "2021-01-22", "21", "01"),
("Pub amarillo", "iuy369", "calle cuatro 14", "2020-04-29", "21", "01");

insert into empleado (DNI_EMPLEADO, NOMBRE, DOMICILIO) 
values
("23132154","Federico","Calle blanca 98"),
("98798778","Jorge","Calle azul 198"),
("4587558","Martin","Calle verde 82"),
("23132165","Agustin","Calle roja 75");

insert into titular (DNI_TITULAR, NOMBRE, DOMICILIO,COD_PUB) 
values
("45213875","Marcelo","Calle franc 98","1"),
("96458745","Luis","Calle ross 198","2"),
("12354445","Florencia","Calle john 82","3"),
("78556452","Mateo","Calle sans 75","4");

insert into existencias (NOMBRE, CANTIDAD, PRECIO, COD_PUB) 
values
("Cerveza","5","5","1"),
("Refresco","15","2.5","2"),
("Tv","2","200","3"),
("Parlante","9","44.85","4");

insert into pub_empleado (DNI_EMPLEADO, FUNCION, COD_PUB)
values
("23132154","Mozo","1"),
("98798778","Dependiente","2"),
("4587558","Lava copas","3"),
("23132165","Encargado","4");

show create table 