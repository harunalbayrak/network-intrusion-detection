class Rule:
    def __init__(self,action,sid,protocol,source_ip,source_port,destination_ip,destination_port,message):
        self.action = action
        self.sid = sid
        self.protocol = protocol
        self.source_ip = source_ip
        self.source_port = source_port
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.message = message

    def to_tuple(self):
        return (self.action, self.sid, self.protocol, self.source_ip, self.source_port, self.destination_ip, self.destination_port, self.message)