-- selecting all from both the schemas

SELECT * 
FROM raw. employees; 

SELECT * 
FROM std.employees;


-- selecting the employee details whose punch time is null 
SELECT e.employee_id, e.first_name, e.last_name, e.salary, 
       t.punch_in_time
FROM std.employees e
JOIN std.timerecord t ON e.employee_id = t.employee_id:: INT
WHERE t.punch_in_time IS NULL;

-- knowing whose contact has been expired 
SELECT DISTINCT *
FROM std.employees e
WHERE e.terminated_date < CURRENT_DATE
  AND e.terminated_reason = 'Contract Expired';

-- finding those employee who has the manager assigned to them 
SELECT DISTINCT e.employee_id, e.first_name,e.last_name
FROM std.employees e
WHERE e.manager_employee_id IS NOT NULL;

-- grouping people having same department id as 54013
SELECT e.department_id, COUNT(*) as count, e.first_name, e.last_name 
FROM std.employees e
WHERE e.department_id='54013'
GROUP BY e.department_id, e.first_name, e.last_name ;

