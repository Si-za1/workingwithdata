TRUNCATE TABLE std.timerecord;

CREATE TABLE std.timerecord (
  employee_id VARCHAR,
  cost_center VARCHAR,
  punch_in_time TIME,
  punch_out_time TIME,
  punch_apply_date DATE,
  hours_worked FLOAT,
  paycode VARCHAR
);


INSERT INTO std.timerecord (
  employee_id,
  cost_center,
  punch_in_time,
  punch_out_time,
  punch_apply_date,
  hours_worked,
  paycode
)
SELECT 
  employee_id, 
  cost_center, 
  CASE 
      WHEN punch_in_time = 'NaN'  THEN NULL
      ELSE punch_in_time::TIME
    END AS punch_in_time, 
  CASE 
      WHEN punch_out_time = 'NaN' THEN NULL
      ELSE punch_out_time::TIME
    END AS punch_out_time, 
  CASE 
      WHEN punch_apply_date IS NULL THEN NULL
      ELSE punch_apply_date::DATE
    END AS punch_apply_date, 
  CAST (hours_worked AS FLOAT), 
  paycode

FROM raw.timerecord;

