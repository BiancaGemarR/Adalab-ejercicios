USE tienda;
--1. Selecciona el ID, nombre, apellidos de las empleadas y el ID de cada 
--cliente asociado a ellas, usando CROSS JOIN.
SELECT 
    employees.employee_number, 
    employees.first_name, 
    employees.last_name, 
    customers.customer_number
FROM employees
CROSS JOIN customers;

--2. Selecciona el ID, nombre, apellidos de las empleadas, para aquellas con más de 8 clientes, 
--usando CROSS JOIN.
SELECT 
    employees.employee_number, 
    employees.first_name, 
    employees.last_name, 
    COUNT(customer_number)
FROM employees
CROSS JOIN customers
WHERE employees.employee_number = customers.sales_rep_employee_number
GROUP BY employees.employee_number, employees.first_name, employees.last_name
HAVING COUNT(customers.customer_number) > 8;



--3.Selecciona el nombre y apellidos de las empleadas que tienen 
--clientes de más de un país, usando CROSS JOIN.
SELECT 
    employees.first_name, 
    employees.last_name, 
    COUNT(DISTINCT customers.country)
FROM employees
CROSS JOIN customers
WHERE employees.employee_number = customers.sales_rep_employee_number
GROUP BY employees.first_name, employees.last_name
HAVING COUNT(DISTINCT customers.country) > 1;

--4. Selecciona el ID, nombre, apellidos de las empleadas y el ID 
--de cada cliente asociado a ellas, usando INNER JOIN.
SELECT employee_number, first_name, last_name, customers.customer_number
FROM employees
INNER JOIN customers
ON employees.employee_number = customers.sales_rep_employee_number;

--5.Selecciona el ID, nombre, apellidos de las empleadas, para 
--aquellas con más de 8 clientes, usando INNER JOIN.
SELECT employee_number, first_name, last_name
FROM employees
INNER JOIN customers
ON employees.employee_number = customers.sales_rep_employee_number
GROUP BY employee_number, first_name, last_name
HAVING COUNT(customers.customer_number) > 8;

--6. Selecciona el nombre y apellidos de las empleadas que tienen 
--clientes de más de un país, usando INNER JOIN.
SELECT first_name, last_name
FROM employees
INNER JOIN customers
ON employees.employee_number = customers.sales_rep_employee_number
GROUP BY first_name, last_name
HAVING COUNT(DISTINCT customers.country) >1;
