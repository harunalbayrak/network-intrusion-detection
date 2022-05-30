class Alert:
    def __init__(self,time,priority,id,sid,protocol,source_ip,source_port,destination_ip,destination_port,message,contents,class_type,metadata):
        self.time = time
        self.priority = priority
        self.id = id
        self.sid = sid
        self.protocol = protocol
        self.source_ip = source_ip
        self.source_port = source_port
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.message = message
        self.contents = contents
        self.class_type = class_type
        self.metadata = metadata

    def __repr__(self):
        _string = ""
        _string += f"-------------------------------------------\n" 
        _string += f"Time: {self.time}, Priority: {self.priority}\n"
        _string += f"Id: {self.id}, Sid: {self.sid}, Protocol: {self.protocol}\n"
        _string += f"Source IP: {self.source_ip}, Source Port: {self.source_port}\n"
        _string += f"Destination IP: {self.destination_ip}, Destination Port: {self.destination_port}\n"
        _string += f"Message: {self.message}, Contents: {self.contents}\n"
        _string += f"Class Type: {self.class_type}, Metadata: {self.metadata}\n"
        _string += f"-------------------------------------------\n"
        return _string

    def to_tuple(self):
        return (self.time, self.priority, self.id, self.sid, self.protocol, self.source_ip, self.source_port, self.destination_ip, self.destination_port, self.message, self.contents, self.class_type, self.metadata)