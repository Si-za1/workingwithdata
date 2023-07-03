
INSERT INTO std.employees (
  employee_id,
  first_name,
  last_name,
  department_id,
  department_name,
  manager_employee_id,
  employee_role,
  salary,
  hire_date,
  terminated_date,
  terminated_reason,
  dob,
  fte,
  location
)
SELECT
  employee_id::INT,
  first_name,
  last_name,
  department_id::INT,
  department_name,
  CASE 
    WHEN manager_employee_id = '-' THEN NULL
    ELSE CAST(manager_employee_id AS INT)
  END AS manager_employee_id,
  employee_role,
  salary,
  hire_date::DATE,
  CASE
    WHEN terminated_date = '01-01-1700' THEN NULL
    ELSE CAST(terminated_date AS DATE)
  END AS terminated_date,
  terminated_reason,
  dob::DATE,
  CAST(fte AS FLOAT),
  location
FROM raw.employees;
