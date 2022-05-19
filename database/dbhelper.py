import os
import sys
import psycopg2

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from models.rule import Rule
# from models.alert import Alert
import database.dbquery as dbquery

tables = {"rules":0, "alerts":1}

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

    def init_empty_tables(self):
        self.create_rules_table()
        self.create_alerts_table()

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
            sql = dbquery.get_create_query(val)
            self.execute_sql(sql)

    def create_rules_table(self):
        self.drop_table("rules")
        sql = dbquery.get_create_query(tables["rules"])
        self.execute_sql(sql)

    def create_alerts_table(self):
        self.drop_table("alerts")
        sql = dbquery.get_create_query(tables["alerts"])
        self.execute_sql(sql)

    def insert_rule(self, rule):
        self.cursor.execute(dbquery.get_insert_query(tables["rules"]),rule.to_tuple())
        self.conn.commit()

    def insert_alert(self, alert):
        self.cursor.execute(dbquery.get_insert_query(tables["alerts"]),alert.to_tuple())
        self.conn.commit()

    def __del__(self):
        # Closing the connection
        self.conn.close()

