import argparse

from database.dbhelper import DBHelper
from ruleparser.ruleparser import RuleParser
from detection.detection import Detection

# Creates network intrusion detection system
def create_IDS(interface):
    # Creates SQL Tables
    dbHelper = DBHelper()
    dbHelper.init_empty_tables()

    # Parses the signature rules & Inserts the rules to the database
    parser = RuleParser("ruleparser/rules/deneme.rules")
    parser.insert_all_rules_db()

    # Starts the detection algorithm on the specific interface that is given as a parameter
    detection = Detection()
    detection.sniffing(interface)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a network intrusion detection system')
    parser.add_argument('--interface', type=str, required=True, help='The network interface to detect intrusion detection')
    args = parser.parse_args()

    create_IDS(args.interface)