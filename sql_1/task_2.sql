select first_name as 'First Name', last_name as  'Last Name' From employees 

SELECT DISTINCT department_id FROM employees;

SELECT * from employees ORDER BY first_name DESC;

SELECT first_name, last_name, salary *0.12 AS PF FROM employees;

SELECT MAX(salary) AS 'Max Salary', MIN(salary) AS 'Min Salary' FROM employees;

SELECT first_name, last_name, ROUND(salary/ 12, 2) AS 'Monthly Salary' from employees;


