CREATE DATABASE EjercicioAPI

use EjercicioAPI

CREATE TABLE EDITORIAL(
	Id INT PRIMARY KEY,
	CIF CHAR(9),
	RazonSocial VARCHAR(20),
	Direccion VARCHAR(100),
	Web VARCHAR(100),
	Correo VARCHAR(60),
	Telefono VARCHAR(12)
)

CREATE TABLE LIBRO(
	Id INT PRIMARY KEY,
	Precio MONEY,
	ISBN VARCHAR(13),
	Titulo VARCHAR(30),
	NumPaginas INT,
	Temática VARCHAR(15),
	IdEditorial INT
	FOREIGN KEY (IdEditorial) REFERENCES EDITORIAL(Id)
)

CREATE LOGIN alebozek
WITH PASSWORD = 'EjercicioAPI';

CREATE USER alebozek
FOR LOGIN alebozek;

GRANT SELECT, INSERT, UPDATE, DELETE TO alebozek;
exec sp_addrolemember 'db_owner', 'alebozek'

INSERT INTO EDITORIAL VALUES(1, '123456789', 'Planeta Comics', 'C\ Almendralejo 3', 'www.planetacomics.es', 'info@planetacomics.es', '123456789')