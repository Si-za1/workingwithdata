TRUNCATE TABLE  timerecord ;

CREATE TABLE timerecord (
  employee_id VARCHAR,
  cost_center VARCHAR,
  punch_in_time VARCHAR,
  punch_out_time VARCHAR,
  punch_apply_date DATE,
  hours_worked VARCHAR,
  paycode VARCHAR
);