from suricataparser import parse_rule, parse_file, parse_rules

class RuleParser:
    def __init__(self,filename,ignore_comments):
        self.filename = filename
        self.ignore_comments = ignore_comments
        self.total_rules = 0
        self.action = "empty"
        self.header = "empty"
        self.parse_file()

    def __repr__(self):
        max = 1
        string = ''
        for i in range(len(self.rules)):
            if i == max:
                break
            rule = self.rules[i]
            attrs = vars(rule)
            print(', '.join("%s: %s" % item for item in attrs.items()))
            # string = string + f'{rule.sid} - {rule.action} - {rule.header} - {rule.msg} - {rule.content}\n'
        return string

    def parse_file(self):
        self.rules = parse_file(self.filename)

    # Inefficient ? 
    # def read_file(self):
    #     lines = []
    #     with open(self.filename) as f:
    #         lines = f.readlines()

    #     for line in lines:
    #         if(line[0] == '#' and self.ignore_comments == True):
    #             continue
    #         if(line[0] == '\n'):
    #             continue
    #         self.total_rules += 1
    #         # print(f'line {self.total_rules}: {line}')

    #         words = line.split()
    #         for i in range(len(words)):
    #             if i == 0:
    #                 self.action = words[i].replace('#', '')
    #             if i > 0 and i < 7:
    #                 self.header += words[i] + ' '

parser = RuleParser("rules/emerging-all-snort.rules",True)
for x in parser.rules:
    for y in x.options:
        print(f"{y.name} - {y.value}")