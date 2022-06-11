import os
import sys
import re
from suricataparser import parse_rule, parse_file, parse_rules
from idstools import rule

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.rule import Rule
from database.dbhelper import DBHelper
from logger.logger import Logger

class RuleParser:
    def __init__(self,filename):
        self.filename = filename
        self.get_lines(filename)
        self.total_rules = 0
        self.logger = Logger("RULEPARSER")
        self.logger.print_log_info("Signature rules are being parsed...")
        self.parse_file()
        self.logger.print_log_info("Signature rules are parsed!")

    def __repr__(self):
        max = 5
        string = ''
        for i in range(len(self.rules)):
            if i == max:
                break
            string += self.get_rule(i)
        return string

    def get_lines(self,filename):
        file = open(filename, 'r')
        self._lines = []
        temp = file.readlines()
        # temp = [line[:-1] for line in file]
        for x in temp:
            if(x == "\n"):
                continue
            self._lines.append(x)
            # if 'pcre' in x:
            #     print(x)
            #     r1 = re.findall(r'pcre.*;',x)
            #     print(r1[0].split(';')[0][5::].replace("\"",""))

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
        pcre = ""
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
        if 'pcre' in self._lines[i]:
            # print(self._lines[i])
            r1 = re.findall(r'pcre.*;',self._lines[i])
            # print(r1[0].split(';')[0][5::].replace("\"",""))
            pcre = r1[0].split(';')[0][5::].replace("\"","")
            pcre = pcre[1:]
            for c in reversed(pcre):
                if(c != '/'):
                    pcre = pcre[:-1]
                else:
                    break
            pcre = pcre[:-1]
            # if(len(pcre) > 1):
            #     pcre = pcre[1]
            if(len(pcre) > 500 or pcre == '\\'):
                pcre = ""

        rule = Rule(action, sid, protocol, source_ip, source_port, destination_ip, destination_port, message, contents, classtype, pcre, metadata)
        return rule

    def insert_all_rules_db(self):
        self.logger.print_log_info("Signature rules are being added to the database...")
        dbHelper = DBHelper()
        max = 100000
        for i in range(len(self.rules)):
            if i == max:
                break
            rule_object = self.get_rule_object(i)
            # print(self.get_rule(i))
            dbHelper.insert_rule(rule_object)
        self.logger.print_log_info(f"{len(self.rules)} signature rules are added to the database!")

if __name__ == "__main__":
    parser = RuleParser("rules/deneme.rules")
    # print(parser)
    # print(parser)
    parser.logger.print_log_info("Heyyyy")
    parser.insert_all_rules_db()