CREATE DATABASE ejercicio_6;
USE tienda;
SELECT customer_name, phone, address_line1
FROM customers;

SELECT phone, address_line1
FROM customers
WHERE country = "USA";

SELECT contact_last_name, contact_first_name
FROM customers
WHERE address_line2 IS NOT NULL;


