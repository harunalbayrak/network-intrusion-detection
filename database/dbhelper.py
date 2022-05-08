import psycopg2

class DBHelper:
    def __init__(self):
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

    def drop_table(self,table):
        # Doping EMPLOYEE table if already exists.
        self.cursor.execute(f"DROP TABLE IF EXISTS {table}")

    def rules_table(self):
        # Creating table as per requirement
        sql = '''CREATE TABLE RULES(
                        publisher_id SERIAL PRIMARY KEY,
                        publisher_name VARCHAR(255) NOT NULL,
                        publisher_estd INT,
                        publsiher_location VARCHAR(255),
                        publsiher_type VARCHAR(255)
        )'''
        self.cursor.execute(sql)
        print("Rules table created successfully.")
        self.conn.commit()

    def __del__(self):
        # Closing the connection
        self.conn.close()

