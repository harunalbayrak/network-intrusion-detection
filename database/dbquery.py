from venv import create

create_rules_table = """CREATE TABLE RULES(
                        ID SERIAL PRIMARY KEY,
                        ACTION VARCHAR(20) NOT NULL,
                        SID VARCHAR(20) NOT NULL,
                        PROTOCOL VARCHAR(20) NOT NULL,
                        SOURCE_IP VARCHAR(20) NOT NULL,
                        SOURCE_PORT VARCHAR(20) NOT NULL,
                        DESTINATION_IP VARCHAR(20) NOT NULL,
                        DESTINATION_PORT VARCHAR(20) NOT NULL,
                        MESSAGE VARCHAR(255),
                        CONTENTS VARCHAR(255),
                        CLASS_TYPE VARCHAR(50),
                        METADATA VARCHAR(255))"""

insert_rules_table = """INSERT INTO RULES(
                        ACTION, SID, PROTOCOL, SOURCE_IP, SOURCE_PORT,
                        DESTINATION_IP, DESTINATION_PORT, MESSAGE, CONTENTS, CLASS_TYPE, METADATA)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

create_alerts_table = """CREATE TABLE ALERTS(
                        publisher_id SERIAL PRIMARY KEY,
                        publisher_name VARCHAR(255) NOT NULL,
                        publisher_estd INT,
                        publsiher_location VARCHAR(255),
                        publsiher_type VARCHAR(255))"""

insert_alerts_table = """INSERT INTO ALERTS(
                        publisher_id, publisher_name, publisher_estd,
                        publsiher_location, publsiher_type)
                        VALUES (%s,%s,%s,%s,%s)"""

def get_create_query(i):
    match i:
        case 0:
            return create_rules_table
        case 1:
            return create_alerts_table

def get_insert_query(i):
    match i:
        case 0:
            return insert_rules_table
        case 1:
            return insert_alerts_table