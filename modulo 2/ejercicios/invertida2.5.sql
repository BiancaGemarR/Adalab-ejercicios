CREATE SCHEMA ejercicio_5;
USE ejercicio_5;

CREATE TABLE tabla_1 (a INTEGER, b CHAR(10));

RENAME TABLE tabla_1 TO table_2;

ALTER TABLE table_2
MODIFY COLUMN a TINYINT NOT NULL;

ALTER TABLE table_2
CHANGE COLUMN b c CHAR(20);

ALTER TABLE table_2
ADD COLUMN d TIMESTAMP;

ALTER TABLE table_2
DROP COLUMN c;

CREATE TABLE tabla_3 AS
SELECT * FROM table_2;

DROP TABLE IF EXISTS table_2;

RENAME TABLE tabla_3 TO tabla_1;

