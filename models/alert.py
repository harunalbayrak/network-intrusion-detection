class Alert:
    def __init__(self,time,priority,group,threat):
        self.time = time
        self.priority = priority
        self.group = group
        self.threat = threat

    def to_tuple(self):
        return (self.time, self.priority, self.group, self.threat)