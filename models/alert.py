import sqlalchemy as _sql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://docker:docker@localhost/graduation_app"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)
Base = declarative_base()

class Alert(Base):
    __tablename__ = "alerts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    time = _sql.Column(_sql.String, index=True)
    priority = _sql.Column(_sql.String, index=True)
    sid = _sql.Column(_sql.String, index=True)
    protocol = _sql.Column(_sql.String, index=True)
    source_ip = _sql.Column(_sql.String, index=True)
    source_port = _sql.Column(_sql.String, index=True)
    destination_ip = _sql.Column(_sql.String, index=True)
    destination_port = _sql.Column(_sql.String, index=True)
    message = _sql.Column(_sql.String, index=True)
    contents = _sql.Column(_sql.String, index=True)
    class_type = _sql.Column(_sql.String, index=True)
    _metadata = _sql.Column("metadata", _sql.String)

    def __init__(self,time,priority,sid,protocol,source_ip,source_port,destination_ip,destination_port,message,contents,class_type,metadata):
        self.time = time
        self.priority = priority
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
        _string += f"Sid: {self.sid}, Protocol: {self.protocol}\n"
        _string += f"Source IP: {self.source_ip}, Source Port: {self.source_port}\n"
        _string += f"Destination IP: {self.destination_ip}, Destination Port: {self.destination_port}\n"
        _string += f"Message: {self.message}, Contents: {self.contents}\n"
        _string += f"Class Type: {self.class_type}, Metadata: {self.metadata}\n"
        _string += f"-------------------------------------------\n"
        return _string

    def to_tuple(self):
        return (self.time, self.priority, self.sid, self.protocol, self.source_ip, self.source_port, self.destination_ip, self.destination_port, self.message, self.contents, self.class_type, self.metadata)