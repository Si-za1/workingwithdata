import psycopg2
import psycopg2.extras
import pandas as pd


from config import (
    DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME
)


class Connection:
    def __init__(self):
        self.db_connection = None
        self.db_cursor = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        

    def connect(self, schema=None):
        try:
            self.db_connection = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USERNAME,
                password=DB_PASSWORD,
                port=DB_PORT
            )
            if schema:
                self.db_cursor = self.db_connection.cursor()
                self.db_cursor.execute(f"SET search_path TO {schema}")

            self.db_cursor = self.db_connection.cursor()

            print("Connection established successfully")

        except psycopg2.Error as error:
            print("Error while connecting to Postgres:", error)

    def disconnect(self):
        if self.db_cursor:
            self.db_cursor.close()
            self.db_cursor = None
        if self.db_connection:
            self.db_connection.close()
            self.db_connection = None

        print("Disconnected from Postgres")
    
    def execute_query(self, query):
        try:
            self.db_cursor.execute(query)
            self.db_connection.commit()
            print("Query executed successfully!")
        except psycopg2.Error as error:
            self.db_connection.rollback()
            print("Error executing SQL query:", error)


    def create_table(self, table_name, create_table_statement):
        try:
            self.db_cursor.execute(create_table_statement)
            self.db_connection.commit()
            print(f"Table '{table_name}' created successfully!")
        except psycopg2.Error as error:
            print(f"Error creating table '{table_name}':", error)


    def create_tables_from_sql_file(self, sql_file_path):
        try:
            with open(sql_file_path, "r") as f:
                sql_file_content = f.read()

            sql_statements = sql_file_content.split(';')

            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    self.execute_query(statement)

            print(f"Tables created successfully from SQL file: {sql_file_path}")

        except Exception as e:
            print("Error creating tables from SQL file:", e)


    def insert_data(self, table_name, data):
        try:
            schema, table = table_name.split('.')
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            insert_query = f"INSERT INTO \"{schema}\".\"{table}\" ({columns}) VALUES ({', '.join(['%s']*len(data))})"
            self.db_cursor.execute(insert_query, list(data.values()))
            self.db_connection.commit()
            # print("Data inserted successfully!")
        
        except psycopg2.Error as error:
            self.db_connection.rollback()
     