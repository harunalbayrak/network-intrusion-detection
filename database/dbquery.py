from venv import create

create_rules_table = """CREATE TABLE RULES(
                        ID SERIAL PRIMARY KEY,
                        ACTION VARCHAR(20) NOT NULL,
                        SID VARCHAR(20) NOT NULL,
                        PROTOCOL VARCHAR(20) NOT NULL,
                        SOURCE_IP VARCHAR(200) NOT NULL,
                        SOURCE_PORT VARCHAR(80) NOT NULL,
                        DESTINATION_IP VARCHAR(200) NOT NULL,
                        DESTINATION_PORT VARCHAR(80) NOT NULL,
                        MESSAGE VARCHAR(255),
                        CONTENTS VARCHAR(2000),
                        CLASS_TYPE VARCHAR(80),
                        METADATA VARCHAR(500))"""

insert_rules_table = """INSERT INTO RULES(
                        ACTION, SID, PROTOCOL, SOURCE_IP, SOURCE_PORT,
                        DESTINATION_IP, DESTINATION_PORT, MESSAGE, CONTENTS, CLASS_TYPE, METADATA)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

select_rules_table = "SELECT * FROM RULES"

select_rules_table_only_contents = "SELECT contents FROM RULES"

select_rules_table_only_protocol = "SELECT protocol FROM RULES"

select_rules_table_only_src_dest = "SELECT source_ip, source_port, destination_ip, destination_port FROM RULES"

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
                    
select_alerts_table = "SELECT * FROM ALERTS"

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

def get_select_query(i):
    match i:
        case 0:
            return select_rules_table
        case 1:
            return select_alerts_table