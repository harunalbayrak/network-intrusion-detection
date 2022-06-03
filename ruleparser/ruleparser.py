import os
import sys
from suricataparser import parse_rule, parse_file, parse_rules

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.rule import Rule
from database.dbhelper import DBHelper
from logger.logger import Logger

class RuleParser:
    def __init__(self,filename,ignore_comments):
        self.filename = filename
        self.ignore_comments = ignore_comments
        self.total_rules = 0
        self.logger = Logger("RULEPARSER")
        self.parse_file()

    def __repr__(self):
        max = 5
        string = ''
        for i in range(len(self.rules)):
            if i == max:
                break
            string += self.get_rule(i)
        return string

    def parse_file(self):
        self.rules = parse_file(self.filename)
        self.total_rules = len(self.rules)

    def get_rule(self,i):
        contents = []
        string = ''
        rule = self.rules[i]
        string += '-----------------------\n'
        string += f'sid: {rule.sid}\naction: {rule.action}\n'
        header_strings = rule.header.split()
        string += f'protocol: {header_strings[0]}\n'
        string += f'source ip: {header_strings[1]}\n'
        string += f'source port: {header_strings[2]}\n'
        string += f'destination ip: {header_strings[4]}\n'
        string += f'destination port: {header_strings[5]}\n'
        # string += f'sid: {rule.sid}\naction: {rule.action}\nheader: {rule.header}\nmsg: {rule.msg}\n'
        string += '>------ Options ------<\n'
        for y in rule.options:
            if y.name == "content":
                y.value = y.value.replace('"', '').replace('|', '').replace(' ','').lower()
                # string += f'{y.name}: {y.value}\n'
                contents.append(y.value)
                pass
            else:
                string += f'{y.name}: {y.value}\n'
        
        string += f'contents: {contents}\n'
        string += '-----------------------\n'
        return string

    def get_rule_objects(self):
        max = 5
        objects = []
        for i in range(len(self.rules)):
            if i == max:
                break
            objects.append(self.get_rule_object(i))
        return objects

    def get_rule_object(self,i):
        rule = self.rules[i]
        header_strings = rule.header.split()
        sid = rule.sid
        action = rule.action
        protocol = header_strings[0]
        source_ip = header_strings[1]
        source_port = header_strings[2]
        destination_ip = header_strings[4]
        destination_port = header_strings[5],
        message = ""
        contents = []
        classtype = ""
        metadata = ""
        for y in rule.options:
            if y.name == "content":
                y.value = y.value.replace('"', '').replace(' ','').replace('|', ' ').replace('.','').lower()
                # string += f'{y.name}: {y.value}\n'
                if(y.value != ''):
                    contents.append(y.value)
            elif y.name == "msg":
                message = y.value
            elif y.name == "classtype":
                classtype = y.value
            elif y.name == "metadata":
                metadata = y.value.__str__()

        rule = Rule(action, sid, protocol, source_ip, source_port, destination_ip, destination_port, message, contents, classtype, metadata)
        return rule

    def insert_all_rules_db(self):
        dbHelper = DBHelper()
        max = 100000
        print(len(self.rules))
        for i in range(len(self.rules)):
            if i == max:
                break
            rule_object = self.get_rule_object(i)
            # print(self.get_rule(i))
            dbHelper.insert_rule(rule_object)

if __name__ == "__main__":
    parser = RuleParser("rules/deneme.rules",True)
    print(parser)

    # parser.logger.print_log_info("Heyyyy")
    parser.insert_all_rules_db()