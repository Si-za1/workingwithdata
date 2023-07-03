TRUNCATE TABLE std.employees;

CREATE TABLE std.employees (
  employee_id INT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  department_id INT,
  department_name VARCHAR(50),
  manager_employee_id INT,
  employee_role VARCHAR(50),
  salary VARCHAR(50),
  hire_date DATE,
  terminated_date DATE,
  terminated_reason VARCHAR(50),
  dob DATE,
  fte FLOAT,
  location VARCHAR (50)
);
