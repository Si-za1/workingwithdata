import pandas as pd
import json
import xml.etree.ElementTree as ET
from utilis.constants import csv_file, json_file, xml_file
from database.connection import Connection


def read_files():
    try:
        # Read CSV files
        employees_csv_data = pd.read_csv(csv_file[0])
        timerecord_csv_data = pd.concat([pd.read_csv(file) for file in csv_file[1:]])

        # Read JSON file
        with open(json_file, "r") as f:
            json_data = json.load(f)
        json_df = pd.DataFrame(json_data)

        # Read XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Convert XML data to dictionary
        xml_data = []
        for child in root:
            data = {}
            for sub_child in child:
                data[sub_child.tag] = sub_child.text
            xml_data.append(data)

        xml_df = pd.DataFrame(xml_data)

    except Exception as e:
        print("Error while reading files and inserting data into PostgreSQL:", e)


        # Insert data into PostgreSQL tables
    with Connection() as connection:
        schemas = ["raw", "std"]  #defining the schema names
    
        for schema in schemas:
            connection.connect(schema=schema)
            
            # Insert data into 'employees' table
            for _, row in employees_csv_data.iterrows():
                connection.insert_data(f"{schema}.employees", row.to_dict())

            for _, row in json_df.iterrows():
                connection.insert_data(f"{schema}.employees", row.to_dict())

            for row in xml_data:
                connection.insert_data(f"{schema}.employees", row)

            # Insert data into 'timerecord' table
            for _, row in timerecord_csv_data.iterrows():
                connection.insert_data(f"{schema}.timerecord", row.to_dict())

       
    
def create_tables():

    sql_files = [
        "sql/employee.sql",
        "sql/timesheet.sql",
        "sql/std/inserte.sql",
        "sql/std/insertem.sql"
        ]
    try:
        with Connection() as connection:
            for sql_file in sql_files:
                connection.create_tables_from_sql_file(sql_file)
                print("Tables created successfully")

    except Exception as e:
        print("Error while creating tables:", e)


def main():
    create_tables()
    read_files()


if __name__ == "__main__":
    main()


