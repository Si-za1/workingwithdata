HERE, 
We have been provided with 3 different extension files as : json, xml and csv

The task that we were suppose to perform were:
1. Ingest the file directly from the GitHub repository URL. 

2. Utilize pandas DataFrame to load the data

3. Store the URL paths in constants.py file

4. Create two database schemas: raw and std.
        In raw schema, all the tables should have VARCHAR data type.
        In std schema, utilize standard data types.

5. For extraction, extract the raw data directly from the source into the raw schema tables.
    Perform transformations while loading into std schema tables, such as
    Replace ‘-’ with NULL from manager_employee_id
    Perform type case if necessary
    Replace ‘01-01-1700’ dates with NULL from terminated_date 
    And, others if required. 

And, the way I performed these above listed tasks are as follow:

1. Importing Dependencies: Some necessary dependencies were imported as, including psycopg2, psycopg2.extras, and pandas. psycopg2  a PostgreSQL adapter for Python, psycopg2.extras provides extra functionalities, and pandas a data manipulation library.

2. The database connection is made in the PGADMIN4 

3. And, the schemas are also created inside the pgadmin4 

4. So, after the connection has been established, in the run.py the reading of the different extension based files, value insertion in those files,
creation of the files have been performed

5. Whereas, in the Connection.py file the formation of the class and different functions for running the files in the run.py have been created

6. For the raw extraction, it has been performed via the function listed there

7. And, for the data cleaning and the extracted data has been performed via the std

