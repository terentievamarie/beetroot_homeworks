SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id;

SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id
JOIN locations AS l ON d.location_id = l.location_id;

SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id
WHERE e.department_id IN (40, 80);

SELECT d.department_id, d.depart_name, COUNT(e.employee_id) AS num_employees
FROM departments AS d
LEFT JOIN employees AS e ON d.department_id = e.department_id
GROUP BY d.department_id, d.depart_name;

SELECT e.first_name AS employee_first_name, m.first_name AS manager_first_name
FROM employees AS e
LEFT JOIN employees AS m ON e.manager_id = m.employee_id;

SELECT j.job_title, 
       e.first_name || ' ' || e.last_name AS full_name, 
       j.max_salary - e.salary AS salary_difference
FROM employees AS e
JOIN jobs AS j ON e.job_id = j.job_id;

SELECT j.job_title, AVG(e.salary) AS average_salary
FROM employees AS e
JOIN jobs AS j ON e.job_id = j.job_id
GROUP BY j.job_title;

SELECT e.first_name || ' ' || e.last_name AS full_name, e.salary
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id
JOIN locations AS l ON d.location_id = l.location_id
WHERE l.city = 'London';

SELECT d.depart_name, COUNT(e.employee_id) AS num_employees
FROM departments AS d
LEFT JOIN employees AS e ON d.department_id = e.department_id
GROUP BY d.depart_name;