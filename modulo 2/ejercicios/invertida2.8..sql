USE tienda;

--1.Realiza una consulta SELECT que obtenga el número identificativo de cliente más bajo de la base de datos.
SELECT MIN(customer_number)
FROM customers; 
--2. Selecciona el limite de crédito medio para los clientes de España.
SELECT AVG(credit_limit)
FROM customers
WHERE country = 'Spain';

--3.Selecciona el numero de clientes en Francia.
SELECT COUNT(*) AS total_customers
FROM customers
WHERE country = 'France';

--4. Selecciona el máximo de crédito que tiene cualquiera de los clientes del empleado con número 1323.
SELECT MAX(credit_limit)
FROM customers
WHERE sales_rep_employee_number = 1323;

--5.¿Cuál es el número máximo de empleado de la tabla customers?
SELECT MAX(sales_rep_employee_number)
FROM customers;

--6.Realiza una consulta SELECT que seleccione el número de cada empleado de ventas, 
--así como el numero de clientes distintos que tiene cada uno.
SELECT sales_rep_employee_number, COUNT(*) AS clientes_distintos
FROM customers
GROUP BY sales_rep_employee_number;

--7.Selecciona el número de cada empleado de ventas que tenga más de 7 clientes distintos.
SELECT sales_rep_employee_number
FRom customers
GROUP BY sales_rep_employee_number
HAVING COUNT(*) > 7;

--8.Selecciona el número de cada empleado de ventas, así como el numero de clientes distintos que tiene cada uno. 
--Asigna una etiqueta de "AltoRendimiento" a aquellos empleados con mas de 7 clientes distintos.
SELECT sales_rep_employee_number, COUNT(DISTINCT customer_name) AS total_clientes,
CASE
	WHEN COUNT(DISTINCT customer_name) > 7 THEN 'AltoRendimiento'
    END
FROM customers
GROUP BY sales_rep_employee_number;

--9. Selecciona el número de clientes en cada país.
SELECT COUNT(customer_name), country
FROM customers
GROUP BY country;
    
