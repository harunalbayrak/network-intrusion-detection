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
    pass

class PortStatistics(Base):
    __tablename__ = "port_statistics"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    port = _sql.Column(_sql.String, index=True)
    type = _sql.Column(_sql.String, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    pass

class ProtocolStatistics(Base):
    __tablename__ = "protocol_statistics"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    protocol = _sql.Column(_sql.String, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    pass

class ClassTypeStatistics(Base):
    __tablename__ = "class_type_statistics"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    class_type = _sql.Column(_sql.String, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    pass

class DashboardWeekdayStatistics(Base):
    __tablename__ = "dashboard_weekday_statistics"
    weekday = _sql.Column(_sql.Integer, primary_key=True, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    pass

class DashboardRuleStatistics(Base):
    __tablename__ = "dashboard_rule_statistics"
    month_number = _sql.Column(_sql.Integer, primary_key=True, index=True)
    count = _sql.Column(_sql.Integer, index=True)
    pass