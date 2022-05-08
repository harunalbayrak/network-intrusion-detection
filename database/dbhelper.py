import os
import sys
import psycopg2
import dbstr

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.rule import Rule
from models.alert import Alert

tables = {"rules":1, "alerts":2}

rules = [Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode"),Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode"),Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode"),Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode")]
alerts = [Alert("21.05.2018 / 17:56:31","High","Server-MySQL","client overflow attempt"),Alert("21.05.2018 / 17:50:22","High","Server-MySQL","Bittorrent uTP peer request"),Alert("21.05.2018 / 16:42:11","Low","Server-MySQL","OpenSSL TLS change cipher spec protocol denial of service"),Alert("21.05.2018 / 14:54:02","High","Server-MySQL","ssh CRC32 overflow filter"),Alert("21.05.2018 / 10:05:53","Medium","Server-MySQL","Sipvicious User-Agent detected"),Alert("21.05.2018 / 08:44:09","High","Server-MySQL","Win.Trojan.Rombrast Trojan outbound connection")]

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

    def insert_rules_table(self):
        sql = dbstr.get_insert_query(tables["rules"])
        for rule in rules:
            self.cursor.execute(sql, rule)
            self.conn.commit()

    def insert_alerts_table(self):
        sql = dbstr.get_insert_query(tables["alerts"])
        for alert in alerts:
            self.cursor.execute(sql, alert)
            self.conn.commit()

    def __del__(self):
        # Closing the connection
        self.conn.close()

