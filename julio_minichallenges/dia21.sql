/*Eliminar registros: Escribe una consulta SQL para eliminar un usuario específico de la tabla Usuarios.*/
INSERT INTO usuarios(nombre_usuarios)
VALUES ('Maria');


DELETE
FROM usuarios
WHERE id_usuarios = 2;

SELECT * FROM usuarios