create database if not exists viajeros;
use viajeros;

create table if not exists lugar (
CODIGO int auto_increment, 
NOMBRE varchar(25), 
TIPO varchar(25), 
CLIMA varchar(25), 
TOTAL_HABITANTES int,
DESCRIPCION varchar(25),
primary key (CODIGO)
);

create table if not exists pasajero (
CODIGO INT AUTO_INCREMENT, 
NOMBRE varchar(25), 
APELLIDO varchar(25), 
PERFIL varchar(25), 
FECHA_NACIMIENTO date,
NUM_TELEFONICO int, 
L_CODIGO INT,
primary key (CODIGO),
foreign key (L_CODIGO)
	references LUGAR(CODIGO)
);

create table if not exists viaje (
CODIGO INT AUTO_INCREMENT, 
P_CODIGO INT, 
L_CODIGO int,
FECHA date,
primary key (CODIGO),
foreign key (P_CODIGO)
	references PASAJERO(CODIGO),
foreign key (L_CODIGO)
	references LUGAR(CODIGO)
);

insert into lugar (
NOMBRE, 
TIPO, 
CLIMA, 
TOTAL_HABITANTES,
DESCRIPCION)
values 
("Barcelona","Ciudad","Calido","20000","asdasdas"),
("Madrid","Ciudad","Neutro","202000","asdewasdas"),
("Argentina","Pais","Tropical","303000","avbsdasdas"),
("Chile","Pais","Seco","43200","asdjkasdas");

insert into pasajero (
NOMBRE, 
APELLIDO, 
PERFIL, 
FECHA_NACIMIENTO,
NUM_TELEFONICO, 
L_CODIGO)
values 
("Federico","Ara","Turista","1992-05-29","654987321","3"),
("Jorge","Gomez","Primera clase","1995-04-15","632225897","2"),
("Maria","Luan","Lowcost","1987-07-18","684357984","1"),
("Juan","Perez","Turista","2000-06-05","668987458","4");

insert into viaje ( 
P_CODIGO, 
L_CODIGO,
FECHA)
values
("1","2","2022-04-09"),
("2","2","2022-05-17"),
("3","2","2021-06-10"),
("4","3","2022-07-07"),
("1","3","2022-08-05"),
("2","3","2021-05-11"),
("3","4","2022-05-18"),
("4","4","2022-04-22"),
("1","4","2022-04-23"),
("2","1","2021-03-28"),
("3","1","2022-01-06"),
("4","1","2022-11-01"),
("1","1","2022-12-21");

#-------------------------
#1)
select nombre from lugar;
#2)
select nombre, apellido from pasajero;
#3)
select nombre, clima from lugar;
#4)
select nombre, total_habitantes, (total_habitantes+100000) as "incremento + 100000 habitantes" from lugar;
#5)
select nombre, tipo, (total_habitantes*2) as Doble_de_habitantes from lugar;
#6)
select clima from lugar;
#7)
select distinct perfil from pasajero;
#8)
select apellido, perfil from pasajero;
#9)
select nombre, apellido from pasajero where upper(perfil like "turista"); 
#10)
select nombre from lugar where upper(clima like "tropical");
#11)
select nombre from lugar where total_habitantes > 100000000;
#12)
select nombre from pasajero where fecha_nacimiento between "19700101" and "19800101";
#13)
select nombre, fecha_nacimiento as Nacido_el from pasajero where upper(perfil like "bussiness" or perfil like "primera clase");
#14)
select * from lugar where upper(clima not like "Mediterraneo");
#15)
select * from pasajero where upper(nombre like "M%");
#16)
select * from lugar where upper(nombre like "%A%");
#17)
select distinct apellido from pasajero where upper(apellido like "M%O");
#18)
select * from lugar where clima not like "null";
#19)
select * from pasajero where perfil = null;
#20)
select * from pasajero where nombre like "%Y%" and fecha_nacimiento between "19750101" and "19851212";
#21)
select * from pasajero where upper(perfil like "LOW_COST" and apellido like "RUIZ");
#22)
select * from lugar where upper(total_habitantes = null and  nombre like "C%" and (clima like "desconocido" or clima like "mediterraneo"));
#23)
select * from lugar where upper(clima like "desconocido") and (upper(nombre like "%ciudad%") or total_habitantes < 5000000);
#24)
select * from pasajero where fecha_nacimiento < "19700101" and upper(perfil like "bussiness class" and nombre like "%G%");
#25)
select * from lugar where total_habitantes not between 50000000 and 100000000;
#26)
select * from lugar order by total_habitantes desc;
#27)
select concat(apellido," ",nombre) as "Nombre y Apellido" from pasajero order by apellido;
#28)
select * from lugar where upper(clima like "tropical") order by nombre;
#29)
select * from lugar where upper(continente like "europa") order by total_habitantes;
#30)
select * from pasajero;
#31)
select * from 
#32)

#33)

#34)

#35)