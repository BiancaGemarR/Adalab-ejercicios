/*Ejercicio 3: Crea las tabla Empleadas y empleadas_en_proyectos, definiendo claves primarias, 
claves foránea, tipos de datos, etc. Haz que cuando se elimine una Empleada, se eliminen todas las entradas 
en empleadas_en_proyectos asociadas.*/

CREATE SCHEMA ejercicio_3;
USE ejercicio_3; 

CREATE TABLE empleadas(
	id_empleada INT AUTO_INCREMENT,
	salario FLOAT NOT NULL,
	nombre VARCHAR(20) NOT NULL,
	pais VARCHAR(25),
	PRIMARY KEY (id_empleada));


CREATE TABLE empleadas_proyectos(
proyecto_id INT, 
id_empleada INT,
PRIMARY KEY (proyecto_id, id_empleada),
CONSTRAINT fk_empleada
	FOREIGN KEY  (id_empleada)
    REFERENCES empleadas(id_empleada)
    );
