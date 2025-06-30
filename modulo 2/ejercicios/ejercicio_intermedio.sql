CREATE SCHEMA videoclub;
USE videoclub;

CREATE TABLE generos (
	id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nombre_genero VARCHAR(15),
    descripcion LONGTEXT
    );
CREATE TABLE peliculas (
	id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(15),
    duracion INT,
    direccion VARCHAR(35),
    id_genero INT,
    fecha_estreno DATE,
    CONSTRAINT fk_peliculas_genero FOREIGN KEY (id_genero)
    REFERENCES generos(id_genero)
    );
    
CREATE TABLE clientes (
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    apellido VARCHAR(30),
    direccion VARCHAR(30),
    telefono VARCHAR(30),
    email VARCHAR(30),
    fecha_registro VARCHAR(30)
    );
    
CREATE TABLE alquileres (
	id_alquileres INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_pelicula INT,
    fecha_alquiler DATE,
    fecha_devolucion DATE,
    estado ENUM('pendiente', 'devuelto'),
    CONSTRAINT fk_alquileres_cliente FOREIGN KEY (id_cliente)
    REFERENCES clientes(id_cliente),
    CONSTRAINT fk_alquileres_pelicula FOREIGN KEY (id_pelicula)
    REFERENCES peliculas(id_pelicula)
    );
    
ALTER TABLE clientes
MODIFY COLUMN email VARCHAR(45) NOT NULL;

ALTER TABLE alquileres
MODIFY COLUMN estado ENUM('pendiente', 'devuelto') DEFAULT 'pendiente';


INSERT INTO generos (nombre_genero, descripcion)
VALUES ('Acción', 'Películas llenas de emoción y aventuras'),
 ('Comedia', 'Películas para reír y disfrutar'),
 ('Drama', 'Películas emocionales y profundas'),
 ('Ciencia Ficción', 'Películas con elementos futuristas o tecnológicos');

INSERT INTO peliculas (nombre, duracion, direccion, id_genero, fecha_estreno)
	VAlUES ('Misión Rescate', 130, 'Ridley Scott', 4, '2015-10-02'),
 ('Gran Aventura', 120, 'Chris Columbus', 1, '2001-06-22'),
 ('Reír o Llorar', 95, 'John Smith', 2, '2020-11-12'),
 ('Crisis Total', 110, 'Jane Doe', 3, '2019-05-15');
 
 INSERT INTO clientes (nombre, apellido, direccion, telefono, email, fecha_registro)
 VALUES ('Carlos', 'García', 'Av. Principal 123', '555-1234', 'carlos@example.com', '2023-01-15'),
 ('Lucía', 'Pérez', 'Calle Secundaria 45', '555-5678', 'lucia@example.com', '2023-02-20'),
 ('Miguel', 'Lopez', 'Av. Tercera 789', '555-9876', 'miguel@example.com', '2023-03-10');
 
 INSERT INTO alquileres (id_cliente, id_pelicula, fecha_alquiler, fecha_devolucion, estado)
 VALUES (1, 1, '2025-01-01', NULL, 'pendiente'),
 (2, 2, '2025-01-03', '2025-01-07', 'devuelto'),
 (3, 4, '2025-01-05', NULL, 'pendiente');
 
 --Modificaciones y consultas
 UPDATE clientes
 SET email = 'carlos_garcia@example.com'
 WHERE id_cliente = 1;
 
 DELETE FROM alquileres
 WHERE id_cliente = 2;
 DELETE FROM clientes
 WHERE id_cliente = 2;
 
 ALTER TABLE generos
 RENAME COLUMN nombre_genero TO genero;
 
 SELECT * 
 FROM peliculas;

SELECT nombre, duracion
FROM peliculas;

SELECT *
FROM peliculas
WHERE id_pelicula =4; 

SELECT *
FROM clientes
WHERE nombre = 'Carlos';

SELECT nombre, fecha_estreno
FROM peliculas
ORDER BY fecha_estreno ASC;

SELECT nombre, fecha_estreno
FROM peliculas
ORDER BY fecha_estreno DESC;

SELECT *
FROM peliculas
LIMIT 2;

SELECT *
FROM peliculas
WHERE duracion BETWEEN 90 AND 120;

SELECT *
FROM peliculas
WHERE duracion >100 OR id_pelicula =1;

SELECT *
FROM peliculas
WHERE duracion >100 OR id_genero =1;

SELECT *
FROM alquileres
WHERE fecha_devolucion IS NOT NULL; 
--No me da nada porque antes nos hemos cargado los registros

SELECT DISTINCT genero
FROM generos;

