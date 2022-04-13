from suricataparser import parse_rule, parse_file, parse_rules

rules = parse_file("rules/emerging-all-snort.rules")

print(len(rules))
