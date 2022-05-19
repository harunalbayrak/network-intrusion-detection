from suricataparser import parse_rule, parse_file, parse_rules

class RuleParser:
    def __init__(self,filename,ignore_comments):
        self.filename = filename
        self.ignore_comments = ignore_comments
        self.total_rules = 0
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

parser = RuleParser("rules/emerging-all-snort.rules",True)
print(parser)
    