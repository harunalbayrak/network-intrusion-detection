import sqlalchemy as _sql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://docker:docker@localhost/graduation_app"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)
Base = declarative_base()

class IPStatistics(Base):
    __tablename__ = "ip_statistics"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    ip = _sql.Column(_sql.String, index=True)
    country = _sql.Column(_sql.String, index=True)
    type = _sql.Column(_sql.String, index=True)
    count = _sql.Column(_sql.Integer, index=True)

    def __init__(self,ip,country,type,count):
        self.ip = ip
        self.country = country
        self.type = type
        self.count = count

    def to_tuple(self):
        return (self.ip, self.country, self.type, self.count, self.ip, self.type)

class PortStatistics(Base):
    __tablename__ = "port_statistics"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    port = _sql.Column(_sql.String, index=True)
    type = _sql.Column(_sql.String, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    
    def __init__(self,port,type,count):
        self.port = port
        self.type = type
        self.count = count

    def to_tuple(self):
        return (self.port, self.type, self.count, self.port)

class ProtocolStatistics(Base):
    __tablename__ = "protocol_statistics"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    protocol = _sql.Column(_sql.String, index=True)
    count = _sql.Column(_sql.Integer, index=True)

    def __init__(self,protocol,count):
        self.protocol = protocol
        self.count = count

    def to_tuple(self):
        return (self.protocol, self.count, self.protocol)

class ClassTypeStatistics(Base):
    __tablename__ = "class_type_statistics"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    class_type = _sql.Column(_sql.String, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    
    def __init__(self,class_type,count):
        self.class_type = class_type
        self.count = count

    def to_tuple(self):
        return (self.class_type, self.count)

class DashboardWeekdayStatistics(Base):
    __tablename__ = "dashboard_weekday_statistics"
    weekday = _sql.Column(_sql.Integer, primary_key=True, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    
    def __init__(self,weekday,count):
        self.weekday = weekday
        self.count = count

    def to_tuple(self):
        return (self.weekday, self.count)

    def to_tuple2(self):
        return (self.count, self.weekday)
        
class DashboardRuleStatistics(Base):
    __tablename__ = "dashboard_rule_statistics"
    month_number = _sql.Column(_sql.Integer, primary_key=True, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    
    def __init__(self,month_number,count):
        self.month_number = month_number
        self.count = count

    def to_tuple(self):
        return (self.month_number, self.count)