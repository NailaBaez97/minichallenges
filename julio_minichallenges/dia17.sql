/*Creaci�n de tabla: Escribe una consulta SQL para crear una tabla Usuarios con columnas id y nombre.*/
CREATE DATABASE minichallenges

CREATE TABLE usuarios(
	id_usuarios INT IDENTITY(1,1) PRIMARY KEY,
	nombre_usuarios VARCHAR(50)
);