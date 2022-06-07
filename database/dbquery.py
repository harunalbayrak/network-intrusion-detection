from venv import create

# RULES
create_rules_table = """CREATE TABLE RULES(
                        ID SERIAL PRIMARY KEY,
                        ACTION VARCHAR(20) NOT NULL,
                        SID VARCHAR(20) NOT NULL,
                        PROTOCOL VARCHAR(20) NOT NULL,
                        SOURCE_IP VARCHAR(500) NOT NULL,
                        SOURCE_PORT VARCHAR(80) NOT NULL,
                        DESTINATION_IP VARCHAR(500) NOT NULL,
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

# ALERTS
create_alerts_table = """CREATE TABLE ALERTS(
                        ID SERIAL PRIMARY KEY,
                        TIME VARCHAR(20) NOT NULL,
                        DAY VARCHAR(20) NOT NULL,
                        PRIORITY VARCHAR(20) NOT NULL,
                        SID VARCHAR(20) NOT NULL,
                        PROTOCOL VARCHAR(20) NOT NULL,
                        SOURCE_IP VARCHAR(30) NOT NULL,
                        SOURCE_PORT VARCHAR(10) NOT NULL,
                        DESTINATION_IP VARCHAR(30) NOT NULL,
                        DESTINATION_PORT VARCHAR(10) NOT NULL,
                        MESSAGE VARCHAR(255),
                        CONTENTS VARCHAR(2000),
                        CLASS_TYPE VARCHAR(80),
                        METADATA VARCHAR(500))"""

insert_alerts_table = """INSERT INTO ALERTS(
                        TIME, DAY, PRIORITY, SID, PROTOCOL, SOURCE_IP, SOURCE_PORT,
                        DESTINATION_IP, DESTINATION_PORT, MESSAGE, CONTENTS, CLASS_TYPE, METADATA)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

select_alerts_table = "SELECT * FROM ALERTS"

# IP STATISTICS
create_ip_statistics_table = """CREATE TABLE IP_STATISTICS(
                                ID SERIAL PRIMARY KEY,
                                IP VARCHAR(30) NOT NULL,
                                COUNTRY VARCHAR(50) NOT NULL,
                                TYPE VARCHAR(10) NOT NULL,
                                COUNT INT NOT NULL,
                                """

insert_ip_statistics_table = """INSERT INTO IP_STATISTICS(
                                IP, COUNTRY, TYPE, COUNT)
                                VALUES (%s,%s,%s,%d)"""

select_ip_statistics_table = "SELECT * FROM IP_STATISTICS"

# PORT STATISTICS
create_port_statistics_table = """CREATE TABLE PORT_STATISTICS(
                                ID SERIAL PRIMARY KEY,
                                PORT VARCHAR(30) NOT NULL,
                                TYPE VARCHAR(10) NOT NULL,
                                COUNT INT NOT NULL,
                                """

insert_port_statistics_table = """INSERT INTO PORT_STATISTICS(
                                PORT, TYPE, COUNT)
                                VALUES (%s,%s,%d)"""

select_port_statistics_table = "SELECT * FROM PORT_STATISTICS"                                

# PROTOCOL STATISTICS
create_protocol_statistics_table = """CREATE TABLE PROTOCOL_STATISTICS(
                                    ID SERIAL PRIMARY KEY,
                                    PROTOCOL VARCHAR(30) NOT NULL,
                                    COUNT INT NOT NULL,
                                    """

insert_protocol_statistics_table = """INSERT INTO PROTOCOL_STATISTICS(
                                    PROTOCOL, COUNT)
                                    VALUES (%s,%d)"""

select_protocol_statistics_table = "SELECT * FROM PROTOCOL_STATISTICS"

# CLASS TYPE STATISTICS
create_class_type_statistics_table = """CREATE TABLE CLASS_TYPE_STATISTICS(
                                    ID SERIAL PRIMARY KEY,
                                    CLASS_TYPE VARCHAR(80) NOT NULL,
                                    COUNT INT NOT NULL,
                                    """

insert_class_type_statistics_table = """INSERT INTO CLASS_TYPE_STATISTICS(
                                        CLASS_TYPE, COUNT)
                                        VALUES (%s,%d)"""

select_class_type_statistics_table = "SELECT * FROM CLASS_TYPE_STATISTICS"

# DASHBOARD_WEEKDAY_STATISTICS
create_dashboard_weekday_statistics_table = """CREATE TABLE DASHBOARD_WEEKDAY_STATISTICS(
                                            WEEKDAY INT PRIMARY KEY,
                                            COUNT INT NOT NULL,
                                            """

insert_dashboard_weekday_statistics_table = """INSERT INTO DASHBOARD_WEEKDAY_STATISTICS(
                                            WEEKDAY, COUNT)
                                            VALUES (%d,%d)"""

select_dashboard_weekday_statistics_table = "SELECT * FROM DASHBOARD_WEEKDAY_STATISTICS"


# DASHBOARD_RULE_STATISTICS
create_dashboard_rule_statistics_table = """CREATE TABLE DASHBOARD_RULE_STATISTICS(
                                            MONTH_NUMBER INT PRIMARY KEY,
                                            COUNT INT NOT NULL,
                                            """

insert_dashboard_rule_statistics_table = """INSERT INTO DASHBOARD_RULE_STATISTICS(
                                            MONTH_NUMBER, COUNT)
                                            VALUES (%d,%d)"""

select_dashboard_rule_statistics_table = "SELECT * FROM DASHBOARD_RULE_STATISTICS"

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