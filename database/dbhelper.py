import os
import sys
import psycopg2

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from models.rule import Rule
# from models.alert import Alert
from logger.logger import Logger
import database.dbquery as dbquery

tables = {"rules":0, "alerts":1, "ip_statistics":2, "port_statistics":3, "protocol_statistics":4, "class_type_statistics":5, "dashboard_weekday_statistics":6, "dashboard_rule_statistics":7}

class DBHelper:
    def __init__(self):
        self.logger = Logger("DATABASE")
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
        self.create_tables()

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.print_log_error(f"{error}")
        finally:
            self.logger.print_log_info(f"{sql} command executed successfully.")

    def execute_sql2(self, sql, args):
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.print_log_error(f"{error}")
        # finally:
            # self.logger.print_log_info(f"{sql} command executed successfully.")

    def drop_table(self,table):
        # Doping EMPLOYEE table if already exists.
        self.cursor.execute(f"DROP TABLE IF EXISTS {table}")

    def create_tables(self):
        for key, val in tables.items():
            self.drop_table(key)
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
        self.execute_sql2(dbquery.get_insert_query(tables["rules"]),rule.to_tuple())
        
    def insert_alert(self, alert):
        self.execute_sql2(dbquery.get_insert_query(tables["alerts"]),alert.to_tuple())

    def insert_statistics(self, num, statistics):
        self.execute_sql2(dbquery.get_insert_query(num),statistics.to_tuple())

    def select_rules(self):
        self.cursor.execute(dbquery.get_select_query(tables["rules"]))
        records = self.cursor.fetchall()
        return records

    def select_rules_only_contents(self):
        self.cursor.execute(dbquery.select_rules_table_only_contents)
        records = self.cursor.fetchall()
        return records

    def select_rules_only_protocol(self):
        self.cursor.execute(dbquery.select_rules_table_only_protocol)
        records = self.cursor.fetchall()
        return records

    def select_rules_only_src_dst(self):
        self.cursor.execute(dbquery.select_rules_table_only_src_dest)
        records = self.cursor.fetchall()
        return records

    def select_statistics(self, num):
        self.cursor.execute(dbquery.get_select_query(num))
        records = self.cursor.fetchall()
        return records

    def select_weekday(self, weekday):
        self.cursor.execute(dbquery.select_dashboard_weekday_statistics_table_2,str(weekday))
        record = self.cursor.fetchone()
        return record

    def update_statistics(self, num, statistics):
        self.execute_sql2(dbquery.get_update_query(num),statistics)

    def __del__(self):
        # Closing the connection
        self.conn.close()

