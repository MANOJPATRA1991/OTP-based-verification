from sqlalchemy import (Column, BigInteger, Integer,
                        String, Boolean, DateTime)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'mobileusers'

    id = Column(Integer, primary_key=True)
    mobile_no = Column(BigInteger, unique=True, nullable=False)
    otp = Column(Integer, nullable=False)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

engine = create_engine('postgresql://dbuser:users@localhost/mobileusers')


Base.metadata.create_all(engine)