create database if not exists encriptar;
drop table if exists clientes;
create table clientes(
nombre varchar(50),
mail varchar(70),
tarjetacredito blob,
primary key (nombre)
);
insert into clientes
values ('Marcos Luis','marcosluis@gmail.com',aes_encrypt('5390700823285988','xyz123'));
insert into clientes
values ('Ganzalez Ana','gonzalesa@gmail.com',aes_encrypt('4567230823285445','xyz123'));
insert into clientes
values ('Lopez German','lopezg@yahoo.com',aes_encrypt('7840704453285443','xyz123'));
-- Si accedemos al campo tarjetacredito podemos comprobar que seencuentra cifrado.
select tarjetacredito from clientes;
-- Para descifrar la tarjeta de crédito debemos conocer la clave decifrado: 'xyz123':
select cast(aes_decrypt(tarjetacredito, 'xyz123') as char) from clientes;