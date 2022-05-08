class Rule:
    def __init__(self,action,sid,protocol,message):
        self.action = action
        self.sid = sid
        self.protocol = protocol
        self.message = message

    def to_tuple(self):
        return (self.action, self.sid, self.protocol, self.message)