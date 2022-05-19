import os
import sys
import psycopg2

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.rule import Rule
from models.alert import Alert
import database.dbstr as dbstr

tables = {"rules":1, "alerts":2}

class DBHelper:
    def __init__(self):
        try:
            # Establishing the connection
            self.conn = psycopg2.connect(
                database="graduation_app",
                user='docker',
                password='docker',
                host='0.0.0.0',
                port='5432'
            )
            # Creating a cursor object using the cursor() method
            self.cursor = self.conn.cursor()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            print("SQL command executed successfully.")
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def drop_table(self,table):
        # Doping EMPLOYEE table if already exists.
        self.cursor.execute(f"DROP TABLE IF EXISTS {table}")

    def create_tables(self):
        for val in tables.values:
            sql = dbstr.get_create_query(val)
            self.execute_sql(sql)

    def create_rules_table(self):
        sql = dbstr.get_create_query(tables["rules"])
        self.execute_sql(sql)

    def create_alerts_table(self):
        sql = dbstr.get_create_query(tables["alerts"])
        self.execute_sql(sql)

    def insert_rule(self, rule):
        self.cursor.execute(dbstr.get_insert_query(0),rule.to_tuple())
        self.conn.commit()

    def insert_alert(self, alert):
        self.cursor.execute(dbstr.get_insert_query(1),alert.to_tuple())
        self.conn.commit()

    def __del__(self):
        # Closing the connection
        self.conn.close()

