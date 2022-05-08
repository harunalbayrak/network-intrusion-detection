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