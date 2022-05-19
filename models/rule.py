import os
import sys
import sqlalchemy as _sql

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://docker:docker@localhost/graduation_app"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)
Base = declarative_base()

class Rule(Base):
    __tablename__ = "rules"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    action = _sql.Column(_sql.String, index=True)
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

    def __init__(self,action,sid,protocol,source_ip,source_port,destination_ip,destination_port,message,contents,class_type,metadata):
        self.action = action
        self.sid = sid
        self.protocol = protocol
        self.source_ip = source_ip
        self.source_port = source_port
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.message = message
        self.contents = ' '.join(map(str, contents))
        self.class_type = class_type
        self.metadata = metadata

    def to_tuple(self):
        return (self.action, str(self.sid), self.protocol, self.source_ip, self.source_port,
            self.destination_ip, self.destination_port, self.message, self.contents, self.class_type, self.metadata)