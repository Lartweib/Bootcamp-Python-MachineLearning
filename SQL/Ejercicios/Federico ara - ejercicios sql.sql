#1) Crea una base de datos nueva.
#2) Al crear la tablas verifica existencia
#3) Se solicita la creación de las tablas teniendo en cuenta las siguientes restricciones:
#• Todos los valores son de tipo carácter excepto los campos F_APERTURA(fecha) , CANTIDAD, PRECIO y COD_LOCALIDAD (numéricos).
#• Los únicos campos que no son obligatorios son los campos DOMICILIO.
#• Los valores del campo horario sólo pueden ser HOR1, HOR2 y HOR3.
#• No es posible dar de alta STOCK a precio 0.
#• El campo CARGO de la tabla PUB_EMPLEADO sólo puede tener los valores CAMARERO, SEGURIDAD, LIMPIEZA.
#• Se ha de mantener la integridad referencial entre las tablas.
#• Las claves primarias vienen marcadas en rojo.

create database if not exists pub; 

use pub;

create table if not exists pub (
COD_PUB varchar(25),
NOMBRE varchar(25) not null,
LICENCIA_FISCAL varchar(25) not null,
DOMICILIO varchar(25) ,
FECHA_APERTURA date not null,
HORARIO enum("HOR1","HOR2","HOR3") not null,
COD_PROV int not null,
primary key (COD_PUB),
foreign key (COD_PROV)
	references pub.localidad(COD_PROV)
);

create table if not exists titular (
DNI_TITULAR varchar(25) ,
NOMBRE varchar(25) not null,
DOMICILIO varchar(25) ,
COD_PUB varchar(25) not null,
primary key (DNI_TITULAR),
foreign key (COD_PUB)
	references pub.pub(COD_PUB)
);

create table if not exists empleado (
DNI_EMPLEADO varchar(25),
NOMBRE varchar(25) not null,
DOMICILIO varchar(25),
primary key (DNI_EMPLEADO)
);

drop table if exists localidad;
create table if not exists localidad (
COD_PROV int,
NOMBRE varchar(25) not null,
primary key (COD_PROV)
);

create table if not exists stock (
COD_PROD varchar(25),
NOMBRE varchar(25) not null,
CANTIDAD int not null,
PRECIO int not null,
constraint precio check(precio>0),
COD_PUB varchar(25) not null,
primary key (COD_PROD),
foreign key (COD_PUB)
	references pub.pub(COD_PUB)
);

create table if not exists pub_empleado (
COD_PUB varchar(25) not null,
DNI_EMPLEADO varchar(25) not null,
CARGO enum("CAMARERO","SEGURIDAD","LIMPIEZA") not null,
primary key (COD_PUB, DNI_EMPLEADO, CARGO),
foreign key (COD_PUB)
	references pub.pub(COD_PUB),
foreign key (DNI_EMPLEADO)
	references pub.empleado(DNI_EMPLEADO)
);

#4) Crea entradas en cada una de las tablas.
insert into localidad (COD_PROV, NOMBRE) 
values 
("01","Barcelona"),("02","Hospitalet"),("03","Barceloneta"),("04","Florida");

insert into pub (COD_PUB ,NOMBRE, LICENCIA_FISCAL, DOMICILIO, FECHA_APERTURA, HORARIO, COD_PROV) 
values 
("01","Pub verde", "asd456", "calle uno 23", "2021-05-12", "HOR1", "01"),
("02","Pub rojo", "qwe485", "calle dos 52", "2020-02-01", "HOR1", "01"),
("03","Pub azul", "bvc458", "calle tres 96", "2021-01-22", "HOR2", "01"),
("04","Pub amarillo", "iuy369", "calle cuatro 14", "2020-04-29", "HOR3", "01");

insert into empleado (DNI_EMPLEADO, NOMBRE, DOMICILIO) 
values
("23132154","Federico","Calle blanca 98"),
("98798778","Jorge","Calle azul 198"),
("4587558","Martin","Calle verde 82"),
("23132165","Agustin","Calle roja 75");

insert into titular (DNI_TITULAR, NOMBRE, DOMICILIO,COD_PUB) 
values
("45213875","Marcelo","Calle franc 98","01"),
("96458745","Luis","Calle ross 198","02"),
("12354445","Florencia","Calle john 82","03"),
("78556452","Mateo","Calle sans 75","04");

insert into stock (COD_PROD, NOMBRE, CANTIDAD, PRECIO, COD_PUB) 
values
("AB04","Cerveza","5","5","01"),
("AC03","Refresco","15","2.5","02"),
("AE01","Tv","2","200","03"),
("AD02","Parlante","9","44.85","04");

insert into pub_empleado (DNI_EMPLEADO, CARGO, COD_PUB)
values
("23132154","CAMARERO","01"),
("98798778","SEGURIDAD","02"),
("4587558","SEGURIDAD","03"),
("23132165","LIMPIEZA","04");

#5)Altera la estructura de alguna tabla.
#a)Añade un campo nuevo
alter table titular add APELLIDO varchar(25);
update titular set apellido = "Gomez";
#b)Elimina algún campo
ALTER TABLE titular DROP COLUMN apellido ;
#c)Modifica el tipo de algún campo
alter table titular modify DOMICILIO varchar(50);

#6)Crea una nueva restrición
ALTER TABLE titular ADD constraint check(length(domicilio)<=50);

#7)Realizar 6 consultas con su enunciado y script de la solución. De menor a mayor dificultad.
#a)2 básicas con función de agregado
select count(*) as "empleados pub" from pub_empleado;
select max(precio) as "precio maximo", min(precio) as "precio minimo" from stock;
#b)2 entre dos tablas
select p.nombre as Pub, pe.cargo as Cargos
from pub p, pub_empleado pe;
select p.nombre as Pub, pe.cargo as Cargos, e.nombre as empleado
from pub p, pub_empleado pe, empleado e;

#c)2 utilizando JOIN
select p.nombre as Pub, pe.cargo as Cargos
from pub p
join pub_empleado pe
on p.cod_pub = pe.cod_pub;
select p.nombre as Pub, pe.cargo as Cargos, e.nombre as empleado
from pub p
join pub_empleado pe
on p.cod_pub = pe.cod_pub
join empleado e
on e.dni_empleado = pe.dni_empleado;
