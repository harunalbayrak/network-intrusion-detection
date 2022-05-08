import os
import sys
import psycopg2

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.rule import Rule
from models.alert import Alert

create_rules_table = '''CREATE TABLE RULES(
                        publisher_id SERIAL PRIMARY KEY,
                        publisher_name VARCHAR(255) NOT NULL,
                        publisher_estd INT,
                        publsiher_location VARCHAR(255),
                        publsiher_type VARCHAR(255))'''

create_alerts_table = '''CREATE TABLE ALERTS(
                        publisher_id SERIAL PRIMARY KEY,
                        publisher_name VARCHAR(255) NOT NULL,
                        publisher_estd INT,
                        publsiher_location VARCHAR(255),
                        publsiher_type VARCHAR(255))'''

class DBHelper:
    def __init__(self):
        try:
            # Establishing the connection
            self.conn = psycopg2.connect(
                database="databasename",
                user='username',
                password='password',
                host='hostname',
                port='5432'
            )
            # Creating a cursor object using the cursor() method
            self.cursor = self.conn.cursor()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def drop_table(self,table):
        # Doping EMPLOYEE table if already exists.
        self.cursor.execute(f"DROP TABLE IF EXISTS {table}")

    def rules_table(self):
        # Creating table as per requirement
        sql = create_rules_table
        self.cursor.execute(sql)
        print("Rules table created successfully.")
        self.conn.commit()

    def alerts_table(self):
        # Creating table as per requirement
        sql = create_alerts_table
        self.cursor.execute(sql)
        print("Rules table created successfully.")
        self.conn.commit()

    def __del__(self):
        # Closing the connection
        self.conn.close()

