TRUNCATE TABLE raw.employees CASCADE;


CREATE TABLE raw.employees (
  employee_id VARCHAR,
  first_name VARCHAR,
  last_name VARCHAR,
  department_id VARCHAR,
  department_name VARCHAR,
  manager_employee_id VARCHAR,
  employee_role VARCHAR,
  salary VARCHAR,
  hire_date VARCHAR,
  terminated_date VARCHAR,
  terminated_reason VARCHAR,
  dob VARCHAR,
  fte VARCHAR,
  location VARCHAR
);
